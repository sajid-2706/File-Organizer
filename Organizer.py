# This program will organize the files in the current directory into different folders based on their file types. 
# It will create folders for PDFs, Images, DOCS, ZIPs, MP3s, PYTHON files and OTHERS if they do not already exist, and then move the files into the appropriate folders.

#importing the os and shutil modules
import os as o
import shutil as s
#defining the folder to organize and getting the list of files in that folder
folder="."
files=o.listdir(folder)
#creating folders for different file types if they do not already exist
if not o.path.exists("PDFs"):
    o.mkdir("PDFs")
if not o.path.exists("Images"):
    o.mkdir("Images")
if not o.path.exists("DOCS"):
    o.mkdir("DOCS")
if not o.path.exists("ZIPs"):
    o.mkdir("ZIPs")
if not o.path.exists("MP3"):
    o.mkdir("MP3")
if not o.path.exists("PYTHON"):
    o.mkdir("PYTHON")
if not o.path.exists("OTHERS"):
    o.mkdir("OTHERS")
#Looping through the files and moving them to the appropriate folders based on their file extensions
for file in files:
   #ignoring directories and only processing files
   if o.path.isfile(f"{folder}/{file}"):
    #checking the file extension and moving the file to the appropriate folder
    if file.endswith(".pdf"):
        s.move(f"{folder}/{file}",f"PDFs/{file}")
        
    elif file.endswith(".jpeg"):
        s.move(f"{folder}/{file}",f"Images/{file}")
        
    elif file.endswith(".txt"):
        s.move(f"{folder}/{file}",f"DOCS/{file}")
    elif file.endswith(".docx"):
        s.move(f"{folder}/{file}",f"DOCS/{file}")
    elif file.endswith(".zip"):
        s.move(f"{folder}/{file}",f"ZIPs/{file}")
    elif file.endswith(".mp3"):
        s.move(f"{folder}/{file}",f"MP3/{file}")
    elif file.endswith(".py"):
        s.move(f"{folder}/{file}",f"PYTHON/{file}")
    else:
        s.move(f"{folder}/{file}",f"OTHERS/{file}")
    