from src.script import Publisher, Gateway, Subscriber

def test_publisher_declaration_without_any_input_should_fail() -> None:
    try:
        Publisher()
    except Exception as e:
        if str(e) == "Publisher.__init__() missing 2 required positional arguments: 'topic' and 'gateway'":
            return True
        raise Exception('Test test_publisher_without_any_input_should_fail FAILED')

def test_publisher_declaration_without_gateway_input_should_fail() -> None:
    try:
        Publisher('TopicTest')
    except Exception as e:
        if str(e) == "Publisher.__init__() missing 1 required positional argument: 'gateway'":
            return True
        raise Exception('Test test_publisher_without_gateway_input_should_fail FAILED')

def test_publisher_declaration_with_topic_name_as_integrer_should_fail() -> None:
    try:
        gate = Gateway()
        Publisher(123, gate)
    except Exception as e:
        if str(e) == "The Publisher topic need to be a string":
            return True
        raise Exception('Test test_publisher_with_topic_name_as_integrer_should_fail FAILED')

def test_publisher_declaration_with_gateway_as_integrer_should_fail() -> None:
    try:
        Publisher('Topictest', 123)
    except Exception as e:
        if str(e) == "The Publisher gateway need to be a Gateway type":
            return True
        raise Exception('Test test_publisher_with_gateway_as_integrer_should_fail FAILED')

def test_publisher_declaration_with_gateway_and_topic_name_should_success() -> None:
    try:
        gate = Gateway()
        p = Publisher('TopicTest', gate)
    except Exception as e:
        raise Exception('Test test_publisher_with_gateway_and_topic_name_should_success FAILED')

def test_publisher_publish_message_name_should_success():
    gate = Gateway()
    pub = Publisher('PubName', gate)
    pub.publish('Message published')
    if gate.message_queue != [{'topic': 'PubName', 'message': 'Message published'}]:
        raise Exception('Test test_publisher_publish_message_name_should_success FAILED')
    
def test_publisher_topic_in_message_queue_should_success():
    gate = Gateway()
    publisher_name = 'PubName'
    pub = Publisher(publisher_name, gate)
    pub.publish('Message published')
    if gate.message_queue[0]['topic'] != publisher_name:
        raise Exception('Test test_publisher_topic_in_message_queue_should_success FAILED')

def test_publisher_message_in_message_queue_should_success():
    gate = Gateway()
    publisher_name = 'PubName'
    pub = Publisher(publisher_name, gate)
    publisher_message = 'Message published'

    pub.publish(publisher_message)
    if gate.message_queue[0]['message'] != publisher_message:
        raise Exception('Test test_publisher_name_in_message_queue_should_success FAILED')
    
test_publisher_declaration_without_any_input_should_fail()
test_publisher_declaration_without_gateway_input_should_fail()
test_publisher_declaration_with_topic_name_as_integrer_should_fail()
test_publisher_declaration_with_gateway_as_integrer_should_fail()
test_publisher_declaration_with_gateway_and_topic_name_should_success()
test_publisher_publish_message_name_should_success()
test_publisher_topic_in_message_queue_should_success()
test_publisher_message_in_message_queue_should_success()

print('All publisher tests were successful')