"""All the generators available for use in the program"""

# Imports go here
import xlrd as xl
import random as rand

def nameAndGender(numFirst, numLast, wantGender=True):
	"""
	Generates names by accessing dataset of first and last names (Found in Name Database folder) along with their associated genders

	Returns list containing first name, gender, and last name in this order
	"""

	# Declare list
	data = {"first name":0, "last name":0, "gender":0}

	# Open file - From databases
	wb = xl.open_workbook("Database/PI Name Dataset.xlsx")
	sheet = wb.sheet_by_index(0)

	# Randomly select first name, then gender to assign to list
	randVal = rand.randint(1, numFirst)
	data["first name"] = (sheet.cell_value(randVal, 0))
	# Check if gender should be included
	if(wantGender):
		data["gender"] = (sheet.cell_value(randVal, 1))

	# Randomly select last name and assign to list
	data["last name"] = (sheet.cell_value(rand.randint(1, numLast), 2))

	# Return list
	return data

def telephone():
	"""Generates random 10 digit phone numbers and returns them as a dictionary entry"""
	num = ""

	# 
	for i in range(1, 11):
		num += str(rand.randint(0, 9))
		if(i < 7 and i % 3 == 0):
			num += "-"

	return {"telephone":num}

def creditCard():
	"""Generates random 16 digit credit card numbers and returns them as a dictionary entry"""
	num = ""

	# Generate the numbers and add a dash for every four digits except at the end
	for i in range(1, 17):
		num += str(rand.randint(0,9))
		if(i < 16 and i % 4 == 0):
			num += "-"

	return {"credit card":num}

def ipAddress():
	"""Generates ip address that is randomly IPv4 or IPv6"""

	choice = rand.randint(0,1)

	if(choice):
		# The formula to generate random IPv4 addresses
		return {"ip address":'.'.join('%s'%rand.randint(0, 255) for i in range(4))}
	else:
		# The formula to generate random IPv6 addresses
		return {"ip address":':'.join('{:x}'.format(rand.randint(0, 2**16 - 1)) for i in range(8))}

	
