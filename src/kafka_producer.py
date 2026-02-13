from kafka import KafkaProducer
import json

KAFKA_TOPIC = 'cdc-topic'
KAFKA_BROKER = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(message):
    producer.send(KAFKA_TOPIC, message)
    producer.flush()
    print(f"Sent message: {message}")

if __name__ == "__main__":
    sample_data = {"name": "Alice", "email": "alice@example.com"}
    send_message(sample_data)
