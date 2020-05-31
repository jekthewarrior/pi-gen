# Imports go here
import json

import generators as gen
import Database.datasetmanager as dsm

# Here lies the Private Information Generator
ans = ""

while(not ans.lower().startswith('y')):
	# Set-up templates and field selection

	# Ask for number of people to generate info for
	num = int(input("Please enter how many people to generate information for: "))

	# Run database check before calling other functions
	numFirst = dsm.numFirsts()
	numLast = dsm.numLasts()

	# Call generators based on selected template and write data to JSON file/git c
	with open("PI.json", "w") as outfile:

		outfile.write("[")

		for i in range(0, num):

			# Using dictionary unpacking method to combine all the generators
			outfile.write(json.dumps({**gen.nameAndGender(numFirst, numLast), **gen.telephone(), **gen.creditCard(), **gen.ipAddress()}, indent=4))
			if(i != num - 1):
				outfile.write(",\n")

		outfile.write("]")

	# Prompt user to quit after each file generation
	ans = input("Do you want to quit?")
