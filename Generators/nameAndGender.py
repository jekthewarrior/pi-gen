# Imports go here
import xlrd as xl
import random as rand

def nameAndGender(numFirst, numLast):
	"""
	Generates names by accessing dataset of first and last names (Found in Name Database folder) along with their associated genders
	
	Returns list containing first name, gender, and last name in this order
	"""
	
	# Declare list
	data = {"first name":0, "last name":0, "gender":0}
	
	# Open file
	wb = xl.open_workbook("Database/PI Name Dataset.xlsx")
	sheet = wb.sheet_by_index(0)
	
	# Randomly select first name, then gender to assign to list
	randVal = rand.randint(1, numFirst)
	data["first name"] = (sheet.cell_value(randVal, 0))
	data["gender"] = (sheet.cell_value(randVal, 1))
	
	# Randomly select last name and assign to list
	data["last name"] = (sheet.cell_value(rand.randint(1, numLast), 2))
	
	# Return list
	return data
