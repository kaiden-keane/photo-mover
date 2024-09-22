# utilization
# first argument is source destination
# second argumetn is destination

import shutil
import os
import sys


FILE_FORMATS = ["jpg", "jpeg", "png", "gif", "pdf", "raw", "tiff", "eps", "cr2", "crw", "nef", "pef"]


def getPaths():
    n = len(sys.argv)
    if n != 3:
        print("invalid amount of arguments")
        print(f"obtained {n-1} arguments when 3 were expected")
    else:
        valid_arguments = True
        if not os.path.isdir(sys.argv[1]):
            print("invalid source directory")
            valid_arguments = False
        if not os.path.isdir(sys.argv[2]):
            print("invalid destination directory")
            valid_arguments = False

    return valid_arguments
    

def find_image(path, dest):
    # recursively finds all images
    files = os.listdir(path)
    for file in files:
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            find_image(new_path, dest)
        else:
            file_format = file.split(".")[-1].lower() # splits file and takes last value
            if file_format in FILE_FORMATS:
                moveImage(path, file, dest)


def moveImage(src_path, file, dest_path):
    source_file = os.path.join(src_path, file)
    filetype = file.split(".")[-1]

    dest_files = os.listdir(dest_path)
    
    i = 1
    duplicate = True
    if file not in dest_files:
        duplicate = False
        destination_file = os.path.join(dest_path, file)
    else:
        name = ".".join(file.split(".")[:-1])
        while duplicate:
            new_filename = name + f" {i}" + "." + filetype
            if new_filename not in dest_files:
                duplicate = False
            else:
                i += 1
        destination_file = os.path.join(dest_path, new_filename)

    print(source_file + " -> " + destination_file)
    shutil.copyfile(source_file, destination_file)


if __name__ == "__main__":
    
    if getPaths() == True:
        source = sys.argv[1]
        destination = sys.argv[2]
        find_image(source, destination)
    