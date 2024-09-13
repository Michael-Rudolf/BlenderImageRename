import sys
import math
import os

#Usage: python3 <destination folder path> <Lowest image number (likely 1)> <Highest image number> <file type>"
#Make sure that the destination folder path ends with /

destination_folder_path = sys.argv[1]
lowest_image_to_rename = int(sys.argv[2])
highest_image_to_rename = int(sys.argv[3]) + 1

for i in range(lowest_image_to_rename, highest_image_to_rename):
        zeros_before_initial_number = 4 - len(str(i))
        old_file_name_string = ""
        for j in range(zeros_before_initial_number):
                old_file_name_string += "0"
        old_file_name_string += str(i) + "." + sys.argv[4]
        new_file_name_string = str(i) + "." + sys.argv[4]
        if os.path.exists(destination_folder_path + old_file_name_string):
                print(f"Renaming {old_file_name_string} into {new_file_name_string}.")
                os.rename(destination_folder_path + old_file_name_string, destination_folder_path + new_file_name_string)


# Sleep to potentially get the user's attention.
os.system("sleep 3") # Don't use time.sleep(3) to reduce dependencies.
print("\033[92mDone\033[0m")
