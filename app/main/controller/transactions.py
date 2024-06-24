import json

from sqlmodel.ext.asyncio.session import AsyncSession
import aio_pika

from app.main.messaging.rabbitmq import get_rabbitmq_connection
from app.main.model.transactions import TransferTransactionNFT


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
        await channel.default_exchange.publish(
            aio_pika.Message(body=message_body.encode()), routing_key=queue_name
        )

async def processing_transfer_db_operations(transaction: TransferTransactionNFT):
    async with AsyncSession() as session:
        async with session.begin():
            pass


async def process_transfer_controller(transfer_payload: dict):
    transaction: TransferTransactionNFT = TransferTransactionNFT(**transfer_payload)
    await publish_message(transaction)
    await processing_transfer_db_operations(transaction)