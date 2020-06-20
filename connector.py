# Imports go here
import kafka as kf
import json

def createProducer(**configOptions):
	"""This initializes a Kafka producer for use in the main function"""

	while(True):
		# Checking to see if the user wants to use a non-default address
		while(True):
			brokerId = input('Would you like to connect to a non-default broker address? (Y/N)')
			if(brokerId.lower().startswith('y')):
				brokerId = input("Please enter your broker address in the format 'host:port' ")
			elif(brokerId.lower().startswith('n')):
				brokerId = 'localhost:9092'
				break

		# Configuring the producer with the necessary arguments
		# The value serializer is given a lambda that converts the sent data into bytes for submission to the cluster
		producer = kf.KafkaProducer(client_id="pii-generator", 
			bootstrap_servers=brokerId, 
			value_serializer=lambda v: json.dumps(v).encode('utf-8'))

		# ! Make sure that this break statement is not cutting the creation of a producer off
		if(producer.bootstrap_connected()):
			break

	return producer

