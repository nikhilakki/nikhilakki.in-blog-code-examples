from confluent_kafka import Producer

p = Producer({"bootstrap.servers": "localhost"})


def delivery_report(err, msg):
    if err is not None:
        print("Message delivery failed: {}".format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))


# Asynchronous message production
p.produce("myTopic", "Hello Kafka!", callback=delivery_report)

# Wait for message delivery
p.flush()
