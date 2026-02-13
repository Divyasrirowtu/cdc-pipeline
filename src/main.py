from kafka_consumer import consumer
from cdc_processor import process_record

def run_pipeline():
    print("Starting CDC pipeline...")
    consumer.consume_messages()

if __name__ == "__main__":
    run_pipeline()
