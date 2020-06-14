# Imports go here
import kafka as kf

def createKafkaProducer():
	"""Creating the Kafka producer to interact with the Kafka cluster"""
	return kf.KafkaProducer()

