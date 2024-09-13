#!/bin/bash


if [[ $1 -eq "" ]]
then
	read -p "The readme is at https://github.com/Michael-Rudolf/blob/main/README.md. Press enter to print the readme or CTRL + C to quit." -n 2 -r
	cat README.md
else
	echo "Checking files in folder: " + $1 + "."
	sleep 1
	python3 find_information_of_folder.py $1
	sleep 1
fi
