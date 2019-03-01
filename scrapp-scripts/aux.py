import os

files = ['extracted_info.txt',
         'final_file.txt']

for myfile in files:
    if os.path.isfile(myfile):
        os.remove(myfile)
        print("File %s deleted" % myfile)
    else:
        print("Error: %s file not found" % myfile)
