# Blender Image Rename


## Description 
Reformates the name of files to be x.png instead of 000x.png.

## Use cases
For example, on a website with 3D animations, it is easier to implement x.png then 000x.png or similiar, however, some applications, like blender don't have an option to change the output name format.
And the amount of files that need to be renamed is high.
This repo can do this automatically.

This repo is named BlenderImageRename, but it can also be used for anything else that uses a similar naming (e.g some cameras).

## Requirements:
- git
- some shell (bash or zsh recommended)
- python3
- python3-os
- python3-sys
- python3-math

## Install
cd into your installation folder of choice, then execute:
> git clone https://github.com/Michael-Rudolf/BlenderImageRename

> cd BlenderImageRename

## Use
Make sure you are in the folder in which you installed BlenderImageRename.
Execute:
> python3 main.py destination_folder lowest_image_number> highest_image_number format

destination folder:
        The folder in which the images that should be renamed are.
lowest image number:
        This should usually be 1.
        This number is the minimum image that will be renamed.
        lowest image number...highest image number is the range in which images will be edited.
highest image number:
        The last image that will be edited.
format:
        The format of what you want to rename. Common: png jpeg jpg pdf.
        This mustn't include a dot before the format.

When everything worked properly, you should see Done.

### Example
You've got photos from a camera in the folder '~/Documents/ImagesFromCamera'.
The first image is named 0000.png and the last one 0185.png.
The command is gonna look like this:
> python3 main.py ~/Documents/ImagesFromCamera/ 0 185 png

## Known problems and future changes
### Command is complicated to use.
I'm working on an easier version with an execution more like:
> ./birename destination_folder
### Not compatible with anything but 4 numbers (0001 works but not 001).
I'm working on it, but there's is a workaround:
Edit the 4 at line 13 column 39 to be however many you need.
