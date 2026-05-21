import os as o
import shutil as s
folder="."
files=o.listdir(folder)
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
for file in files:
   if o.path.isfile(f"{folder}/{file}"):
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
    