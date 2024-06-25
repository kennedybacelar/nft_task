import json

import aio_pika
from sqlalchemy import func, or_
from sqlalchemy.future import select

from app.main.database import get_session
from app.main.database.tables import AssetTable
from app.main.messaging.rabbitmq import get_rabbitmq_connection
from app.main.model.assets import AssetModel
from app.main.model.transactions import (TransactionResponse,
                                         TransactionStatus,
                                         TransferTransactionNFT)
from app.main.utils import InsufficientFundsError


def _formatting_message(transaction: TransferTransactionNFT) -> str:
    return json.dumps(
        {
            "transaction_id": transaction.transaction_id,
            "event_type": transaction.event_type,
            "transaction_status": transaction.transaction_status,
        }
    )


async def publish_message(transaction: TransferTransactionNFT):
    rabbitmq_conn = await get_rabbitmq_connection()
    async with rabbitmq_conn:
        channel = await rabbitmq_conn.channel()
        queue_name = "transaction_events"

        message_body = _formatting_message(transaction)

        await channel.declare_queue(queue_name, durable=True)
        await channel.default_exchange.publish(aio_pika.Message(body=message_body.encode()), routing_key=queue_name)


async def transfering_nft(transaction: TransferTransactionNFT):
    async with get_session() as session:
        async with session.begin():
            stmt = select(AssetTable).where(
                AssetTable.user_wallet == transaction.from_address,
                AssetTable.count > 0,
            )
            result = await session.execute(stmt)
            nft = result.scalars().first()

            if nft is None:
                raise InsufficientFundsError("Insufficient NFT to transfer")

            nft.user_wallet = transaction.to_address


async def fetching_response(transaction: TransferTransactionNFT):
    async with get_session() as session:
        async with session.begin():
            stmt = (
                select(AssetTable.user_wallet, func.sum(AssetTable.count))
                .where(
                    or_(
                        AssetTable.user_wallet == transaction.from_address,
                        AssetTable.user_wallet == transaction.to_address,
                    )
                )
                .group_by(AssetTable.user_wallet)
            )
            result = await session.execute(stmt)
            counts = result.fetchall()

            from_address_wallet_and_count: tuple[str, float] = counts[0]
            to_address_wallet_and_count: tuple[str, float] = counts[1]

        return TransactionResponse(
            transaction_id=transaction.transaction_id,
            event_type=transaction.event_type,
            transaction_status=transaction.transaction_status,
            sender_count=from_address_wallet_and_count[1],
            receiver_count=to_address_wallet_and_count[1],
        )


async def processing_transfer_db_operations(transaction: TransferTransactionNFT) -> TransactionResponse:
    try:
        await transfering_nft(transaction)
        response = await fetching_response(transaction)
        response.transaction_status = TransactionStatus.confirmed
        return response
    except Exception as e:
        transaction.transaction_status = TransactionStatus.failed
    finally:
        await publish_message(transaction)


async def process_transfer_controller(transfer_payload: dict) -> dict:
    transaction: TransferTransactionNFT = TransferTransactionNFT(**transfer_payload)
    await publish_message(transaction)
    response = await processing_transfer_db_operations(transaction)
    return response.model_dump()
