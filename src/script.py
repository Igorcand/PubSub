from typing import Dict, Set, List
from src.mixins import save_publisher_key, save_publisher_messages

class Subscriber:
    '''
    The subscriber just have the update function, they dont care of how will receive the message, they just want to receive the message.
    '''
    def __init__(self, name:str) -> None:
        if not isinstance(name, str):
            raise TypeError('The Subscriber name need to be a string')
        self.name = name
    
    def update(self, topic:str, message:str):
        '''
        The function will show the message received on screen
        '''
        if not isinstance(topic, str):
            raise TypeError('The topic need to be a string')
        if not isinstance(message, str):
            raise TypeError('The message need to be a string')
        
        print(f"| {topic} | {self.name} received: '{message}' ")

class Gateway:
    '''
    The gateway will be resposable to get the subscriber and verify which topic they want to be notified and send to each specific queue
    '''
    def __init__(self) -> None:
        self.subscribers_by_topic: Dict[str, Set] = {}
        self.message_queue: List[Dict[str, str]] = []
    
    def subscribe(self, topic:str, subscriber: Subscriber):
        '''
        If the topic received already exists, the new subscriber will be add in this queue, if not, will create a new key in dictionary to this subscriber
        '''
        if not isinstance(topic, str):
            raise TypeError('To subscribe a publisher queue the topic need to be a string')
        
        if not isinstance(subscriber, Subscriber):
            raise TypeError('The subscriber need to be a Subscriber type')
        
        if topic in self.subscribers_by_topic:
            self.subscribers_by_topic[topic].add(subscriber)
        else:
            self.subscribers_by_topic[topic] = {subscriber}
    
    def receive_message(self, message: Dict[str, str]):
        """ 
        { 'topic': xpto, 'message': xpto } 
        When the gateway realize that someone want to send a message, they will add this message structure on the queue
        """
        self.message_queue.append(message)
    
    def send_message_by_topic(self, topic, message):
        '''
        This function will filter in subscribers_by_topic dictionary and verify inside the quantity of subscriber has inside registred, so will call some function to each subscriber that is the update, that will show on screen.
        '''
        if topic in self.subscribers_by_topic.keys():
            for subscriber in self.subscribers_by_topic[topic]:
                subscriber.update(topic, message)

    
    def broadcast(self):
        '''
        This is the broadcast, who finally will send a message to each subscriber, will call the send_message_by_topic funtion doing the loop for each topic registred
        '''
        for msg in self.message_queue:
            save_publisher_messages(msg['topic'], msg['message'])
            self.send_message_by_topic(msg['topic'], msg['message'])
        
        self.message_queue = []

class Publisher:
    '''
    The publisher just have the publish function, they dont care of how the subscriber will receive the message, they just want to publish the content.
    '''
    def __init__(self, topic:str, gateway: Gateway) -> None:
        if not isinstance(topic, str):
            raise TypeError('The Publisher topic need to be a string')
        
        if not isinstance(gateway, Gateway):
            raise TypeError('The Publisher gateway need to be a Gateway type')
        
        self.topic = topic
        self.mensagens = []
        self.gateway = gateway
        save_publisher_key(topic)
    
    def publish(self, message):
        '''
        Each Publisher just can have one pattern topic, so if they want to send a message, we will send to his gateway the dictionary structure of topic and message
        '''
        msg = {'topic': self.topic, 'message': message}
        self.gateway.receive_message(msg)




