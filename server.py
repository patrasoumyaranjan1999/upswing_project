import pika
import json
import pymongo
from datetime import datetime

# RabbitMQ settings
RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'status_queue'

# MongoDB settings
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB = 'mqtt_data'
MONGO_COLLECTION = 'status_updates'

# Initialize MongoDB client
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def store_status(status_data):
    status_data['timestamp'] = datetime.utcnow()
    collection.insert_one(status_data)
    print(f"Stored in MongoDB: {status_data}")

def on_message(channel, method, properties, body):
    status_data = json.loads(body)
    store_status(status_data)
    channel.basic_ack(delivery_tag=method.delivery_tag)

def start_server():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=on_message)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    start_server()
