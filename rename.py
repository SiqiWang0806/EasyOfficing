import os
import random
import sys
import argparse


parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(usage="[Usage]", description="--path, --FileExt, --start_index")
parser.add_argument("--path", default=".", help="Directory of the file to rename, default is the current directory", dest="path")
parser.add_argument("--FileExt", default="", help="Filetype of the file to rename, default is none :  .txt/.jpg...", dest="FileExt")
parser.add_argument("--start_index", default= 0, help="Pick a number to start ordering, default is 0", dest="start_index")
parser.add_argument("--prefix", default= "", help="Add the Prefix for your file, default is none :  test-/img00 ", dest="prefix")
args = parser.parse_args()
path = args.path
FileExt = args.FileExt
start_index = int(args.start_index)
prefix = args.prefix

file_names = os.listdir(path)


#rename randomly to avoid collision
i=1
rand = str(random.randint(0,10))+"_"
for name in file_names:
    new_name = rand + str(i) + FileExt
    print("Rename filename ["+ name + "] to [" + new_name + "]")
    os.rename((path+name), (path+new_name))
    i = i+1


file_names = os.listdir(path)

i = start_index
for name in file_names:
    new_name = prefix + str(i)+FileExt
    print("Rename filename ["+ name + "] to [" + new_name + "]")
    os.rename((path+name), (path+new_name))
    i = i+1

print("Done! Check files in path: " + path)
