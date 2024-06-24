import aio_pika

from app.main.messaging.rabbitmq import get_rabbitmq_connection


async def process_transfer_controller():
    rabbitmq_conn = await get_rabbitmq_connection()
    async with rabbitmq_conn:
        channel = await rabbitmq_conn.channel()
        queue_name = "transaction_events"
        await channel.declare_queue(queue_name, durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=b"Hello from RabbitMQ!"), routing_key=queue_name
        )
