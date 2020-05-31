# Imports go here
import json

import generators as gen
import Database.datasetmanager as dsm

# Here lies the Private Information Generator
ans = ""

while(not ans.lower().startswith('y')):
	# Set-up templates and field selection

	# Ask to run database check before calling other functions. Otherwise just use variables from the config file
	bop = input("Do you want to run a database check?")

	if(bop.lower().startswith('y')):
		# Perform database check
		numFirst = dsm.numFirsts()
		numLast = dsm.numLasts()
	else:
		# Retrieve previous values from config file
		with open("Database/config.txt", 'r') as infile:
			numFirst = int(infile.readline().strip("\n"))
			numLast = int(infile.readline().strip("\n"))

	# Ask for number of people to generate info for
	num = int(input("Please enter how many people to generate information for: "))

	# Call generators based on selected template and write data to JSON file
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

# Update values in config file, should the database checks have occurred
with open("Database/config.txt", "w") as outfile:
	outfile.write(str(numFirst) + "\n")
	outfile.write(str(numLast) + "")
