# Imports go here
import json

import generators as gen
import Database.datasetmanager as dsm
# connector.py is under development
# import connector as con

# Here lies the main file that provides the user interface to the generators
ans = ""

# Ask to run database check before entering interface loop. Otherwise just use variables from the config file
bop = input("Do you want to run a database check? (Y/N)")

if(bop.lower().startswith('y')):
	# Perform database check
	numFirst = dsm.numFirsts()
	numLast = dsm.numLasts()
else:
	# Retrieve previous values from config file
	with open("Database/config.txt", 'r') as infile:
		numFirst = int(infile.readline().strip("\n"))
		numLast = int(infile.readline().strip("\n"))

while(not ans.lower().startswith('y')):
	# Set-up templates and field selection

	# Ask for number of people to generate info for
	num = int(input("Please enter how many people to generate information for: "))
	
	print("Generating...")
	# Call generators based on selected template and write data to JSON file
	with open("PI.json", "w") as outfile:

		outfile.write("[")

		for i in range(0, num):

			# Using dictionary unpacking method to combine all the generators
			outfile.write(json.dumps({**gen.nameAndGender(numFirst, numLast), **gen.telephone(), **gen.creditCard(), **gen.ipAddress()}, indent=4))
			if(i != num - 1):
				outfile.write(",\n")

		outfile.write("]")
	
	print("File Generated!")
	
	# Prompt user to quit after each file generation
	ans = input("Do you want to quit? (Y/N)")

# Update values in config file, should the database checks have occurred
if(bop.lower().startswith('y')):
	with open("Database/config.txt", "w") as outfile:
		outfile.write(str(numFirst) + "\n")
		outfile.write(str(numLast) + "")
