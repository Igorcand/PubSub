from src.script import Gateway, Publisher, Subscriber

eduardo = Subscriber('Eduardo')
maria = Subscriber('Maria')
jose = Subscriber('José')

gate = Gateway()

cifra_club = Publisher('Cifra Club', gate)
palco_mp3 = Publisher('Palco MP3', gate)

gate.subscribe('Cifra Club', eduardo)
gate.subscribe('Cifra Club', maria)
gate.subscribe('Palco MP3', jose)

cifra_club.publish('É o maior site de ensino de música do Brasil')
palco_mp3.publish('É o maior serviço de música independente do Brasil')

gate.broadcast()

