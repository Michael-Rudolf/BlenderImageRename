# find_information_of_folder.py
# Finds the required information about the image formats
# This includes the name of the first image, the last image and more information about the name format.
# The information will be passed on to main.py

from sys import argv
import os

minimum_value_found = "NaN"
maximum_value_found = "NaN"
zeros = "NaN"
format = "NaF"

destination_folder = argv[1]

if destination_folder[-1]:
    destination_folder += '/'


files_in_destination_folder = os.listdir(destination_folder)

for file_name in files_in_destination_folder:
	file_name_before_prefix = file_name.split(".")[0]
    if isdigit(file_name_before_prefix):
	    value = int(file_name_before_prefix)
	    if minimum_value_found == "NaN":
		    minimum_value_found = value
		    maximum_value_found = value
	    if value > maximum_value_found:
	    	maximum_value_found = value
	    if value < minimum_value_found:
		    minimum_value_found = value
	    zeros = len(file_name_before_prefix)
	    format = file_name.split(".")[1]

if minimum_value_found == "NaN":
	print("ERROR: No correctly formated file found!")
else:
    execution_string = f"python3 main.py {destination_folder} {minimum_value_found} {maximum_value_found} {format}"
    os.system(execution_string)
