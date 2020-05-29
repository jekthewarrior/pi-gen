# Imports go here
import xlrd as xl
import random as rand

def nameAndGender():
	"""
	Generates names by accessing dataset of first and last names (Found in Name Database folder) along with their associated genders
	
	Returns list containing first name, gender, and last name in this order
	"""
	
	# Declare list
	data = []
	
	# Open file
	wb = xl.open_workbook("Name Database/PI Name Dataset.xlsx")
	sheet = wb.sheet_by_index(0)
	
	# Randomly select first name, then gender to assign to list
	# TODO Replace hardcoded value with dynamic function to detect number of rows in column
	randVal = rand.randint(1, 5000)
	data.append(sheet.cell_value(randVal, 0))
	data.append(sheet.cell_value(randVal, 1))
	
	# Randomly select last name and assign to list
	data.append(sheet.cell_value(rand.randint(1, 5000), 2))
	
	# Return list
	return data
