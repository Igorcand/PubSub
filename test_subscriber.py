from src.script import Subscriber

def test_subscriber_without_declaration_name_with_strig_should_fail() -> None:
    try:
        Subscriber()
    except Exception as e:
        if str(e) == "Subscriber.__init__() missing 1 required positional argument: 'name'":
            return True
        raise Exception('Test test_subscriber_without_declaration_name_with_strig_should_fail FAILED')

def test_subscriber_declaration_name_with_strig_should_success() -> None:
    try:
        Subscriber('TestName')
    except Exception as e:
        raise Exception('Test test_subscriber_declaration_name_with_strig_should_success FAILED')

def test_subscriber_declaration_name_with_integer_should_fail() -> None:
    try:
        Subscriber(1234)
    except Exception as e:
        if str(e) == 'The Subscriber name need to be a string':
            return True 
        raise Exception('Test test_subscriber_declaration_name_with_integer_should_fail FAILED')

def test_subscriber_update_topic_and_message_should_success() -> None:
    try:
        topic = 'topic_name'
        message = 'message_name'
        Subscriber('TestName').update(topic, message)
    except Exception as e:
        raise Exception('Test test_subscriber_update_topic_and_message_should_success FAILED')

def test_subscriber_update_topic_as_integer_and_message_should_fail() -> None:
    try:
        topic = 123
        message = 'message_name'
        Subscriber('TestName').update(topic, message)
    except Exception as e:
        if str(e) == 'The topic need to be a string':
            return True 
        raise Exception('Test test_subscriber_update_topic_as_integer_and_message_should_fail FAILED')

def test_subscriber_update_topic_and_message_as_integer_should_fail() -> None:
    try:
        topic = 'topic_name'
        message = 123
        Subscriber('TestName').update(topic, message)
    except Exception as e:
        if str(e) == 'The message need to be a string':
            return True 
        raise Exception('Test test_subscriber_update_topic_as_integer_and_message_should_fail FAILED')

test_subscriber_without_declaration_name_with_strig_should_fail()
test_subscriber_declaration_name_with_strig_should_success()
test_subscriber_declaration_name_with_integer_should_fail()
test_subscriber_update_topic_and_message_should_success()
test_subscriber_update_topic_as_integer_and_message_should_fail()
test_subscriber_update_topic_and_message_as_integer_should_fail()

print('All subscriber tests were successful')
