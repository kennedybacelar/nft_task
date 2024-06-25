from aio_pika import Connection, connect_robust

# RabbitMQ URL
RABBITMQ_URL = "amqp://guest:guest@rabbitmq/"
RABBITMQ_URL = "amqp://guest:guest@localhost:5672/"


async def get_rabbitmq_connection() -> Connection:
    return await connect_robust(RABBITMQ_URL)
