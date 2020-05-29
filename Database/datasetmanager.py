"""Manages the datasets used by the generators"""

# Imports go here
import xlrd as xl

def numFirsts():
	""""Gets the number of first names and associated genders in the appropriate column"""

	wb = xl.open_workbook("Database/PI Name Dataset.xlsx")
	sheet = wb.sheet_by_index(0)

	count = 0

	while(sheet.cell_value(count, 0) != "EOC"):
		count += 1

	return count

def numLasts():
	""""Gets the number of last names in the appropriate column"""
	wb = xl.open_workbook("Database/PI Name Dataset.xlsx")
	sheet = wb.sheet_by_index(0)

	count = 0

	while(sheet.cell_value(count, 2) != "EOC"):
		count += 1

	return count