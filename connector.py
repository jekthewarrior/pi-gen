# Imports go here
import kafka as kf

def kafkaConnector(**configOptions):
	"""A menu to select and connect to Kafka brokers and have an easy menu to conveniently send
	records as a producer to whatever topic and partition needed"""
	return kf.KafkaProducer()

