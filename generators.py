# Imports go here
import xlrd as xl
import random as rand

def nameAndGender(numFirst, numLast, wantGender=True):
	"""
	Generates names by accessing dataset of first and last names (Found in Name Database folder) along with their associated genders
	
	Returns dict containing first name and last name (gender has an option of being included due to the nature of the dataset)
	"""
	
	# Declare dict
	data = {"first name":0, "last name":0, "gender":0}
	
	# Open file
	wb = xl.open_workbook("Database/PI Name Dataset.xlsx")
	sheet = wb.sheet_by_index(0)
	
	# Randomly select first name, then gender to assign to list
	randVal = rand.randint(1, numFirst)
	data["first name"] = (sheet.cell_value(randVal, 0))

	# Check for included gender separation argument
	if(wantGender):
		data["gender"] = (sheet.cell_value(randVal, 1))
	
	# Randomly select last name and assign to list
	data["last name"] = (sheet.cell_value(rand.randint(1, numLast), 2))
	
	# Return dict
	return data

def telephone():
	"""Generates random telephone number and returns as a dict with a single key-value pair"""
	# Prepare string variable for entry
	num = ""

	# Generate and add random telephone numbers
	for i in range(0, 3):
		num += str(rand.randint(0, 9))

	num += "-"

	for i in range(0, 3):
		num += str(rand.randint(0, 9))
	num += "-"

	for i in range(0,4):
		num += str(rand.randint(0, 9))


	return {"telephone":num}