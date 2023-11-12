from src.script import Subscriber, Publisher, Gateway

def test_gateway_subscribe_topic_as_integer_should_fail() -> None:
    try:
        sub = Subscriber('Sub Name')
        gate = Gateway()
        gate.subscribe(123, sub)
    except Exception as e:
        if str(e) == "To subscribe a publisher queue the topic need to be a string":
            return True
        raise Exception('Test test_gateway_subscribe_topic_as_integer_should_fail FAILED')

def test_gateway_subscribe_with_subscriber_as_integer_should_fail() -> None:
    try:
        gate = Gateway()
        gate.subscribe('Pub Topic', 123)
    except Exception as e:
        if str(e) == "The subscriber need to be a Subscriber type":
            return True
        raise Exception('Test test_gateway_subscribe_with_subscriber_as_integer_should_fail FAILED')

def test_gateway_subscribe_with_subscriber_and_topic_correct_should_success() -> None:
    try:
        sub = Subscriber('Sub Name')
        gate = Gateway()
        gate.subscribe('Pub Topic', sub)
    except Exception as e:
        raise Exception('Test test_gateway_subscribe_with_subscriber_and_topic_correct_should_success FAILED')

def test_gateway_subscribe_with_new_topic_should_success() -> None:
    sub = Subscriber('Sub Name')
    gate = Gateway()
    topic_name = 'Pub Topic'
    gate.subscribe(topic_name, sub)
    if len(gate.subscribers_by_topic[topic_name]) != 1:
        raise Exception('Test test_gateway_subscribe_with_new_topic_should_success FAILED')

def test_gateway_subscribe_2_subscribers_in_one_topic_should_success() -> None:
    sub = Subscriber('Sub Name')
    sub2 = Subscriber('Sub Name2')
    gate = Gateway()
    topic_name = 'Pub Topic'
    gate.subscribe(topic_name, sub)
    gate.subscribe(topic_name, sub2)
    if len(gate.subscribers_by_topic[topic_name]) != 2:
        raise Exception('Test test_gateway_subscribe_2_subscribers_in_one_topic_should_success FAILED')
    
def test_gateway_subscribe_with_new_topic_with_subscriber_should_success() -> None:
    sub = Subscriber('Sub Name')
    gate = Gateway()
    topic_name = 'Pub Topic'
    gate.subscribe(topic_name, sub)
    if sub.name != next(iter(gate.subscribers_by_topic[topic_name])).name:
        raise Exception('Test test_gateway_subscribe_with_new_topic_with_subscriber_should_success FAILED')

def test_gateway_broadcast_without_publish_should_success() -> None:
    try:
        sub = Subscriber('Sub Name')
        gate = Gateway()
        gate.subscribe('Pub Topic', sub)
        gate.broadcast()
    except Exception as e:
        raise Exception('Test test_gateway_broadcast_without_publish_should_success FAILED')

def test_gateway_broadcast_subcribe_without_have_publisher_should_success() -> None:
    try:
        sub = Subscriber('SubName')
        gate = Gateway()
        topic_name = 'MP3'
        gate.subscribe(topic_name, sub)
        gate.broadcast()
    except Exception as e:
        raise Exception('Test test_gateway_broadcast_subcribe_without_have_publisher_should_success FAILED')

def test_gateway_broadcast_publish_message_without_have_subscriber_should_success() -> None:
    try:
        sub = Subscriber('SubName')
        gate = Gateway()
        publisher_name = 'PubName'
        pub = Publisher(publisher_name, gate)
        pub.publish('Message published')
        gate.broadcast()
    except Exception as e:
        raise Exception('Test test_gateway_broadcast_publish_message_without_have_subscriber_should_success FAILED')
    
test_gateway_subscribe_topic_as_integer_should_fail()
test_gateway_subscribe_with_subscriber_as_integer_should_fail()
test_gateway_subscribe_with_subscriber_and_topic_correct_should_success()
test_gateway_subscribe_with_new_topic_should_success()
test_gateway_subscribe_2_subscribers_in_one_topic_should_success()
test_gateway_subscribe_with_new_topic_with_subscriber_should_success()
test_gateway_broadcast_without_publish_should_success()
test_gateway_broadcast_subcribe_without_have_publisher_should_success()
test_gateway_broadcast_publish_message_without_have_subscriber_should_success()

print('All gateway tests were successful')