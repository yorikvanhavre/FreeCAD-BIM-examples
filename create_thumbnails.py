#!/usr/bin/python

import sys
import os
import zipfile
import subprocess


# save thumbnails from each file
for fcstd in [f for f in  os.listdir() if f.endswith(".FCStd")]:

    # Read compressed file
    zfile = zipfile.ZipFile(fcstd)
    files = zfile.namelist()

    # Check whether we have a FreeCAD document
    if "Document.xml" not in files:
        print(fcstd, "doesn't look like a FreeCAD file")
        continue

    # Read thumbnail from file or use default icon
    image = "thumbnails/Thumbnail.png"
    if image in files:
        image = zfile.read(image)
    else:
        print(fcstd, "no thumbnail in this file")
        continue

    # Write icon to output_file
    thumb = open(fcstd.replace(".FCStd",".png"), "wb")
    thumb.write(image)
    thumb.close()
    
# create the montage
command = "montage -background #ffffff -fill #000000 -label %t -font Helvetica -pointsize 10 -define png:size=128x128 -geometry 128x128+2+2 -auto-orient -tile 6x *.png contact-sheet.jpg"
subprocess.run(command.split(" "))
    
# delete intermediary files
for png in [f for f in  os.listdir() if f.endswith(".png")]:
    os.remove(png)
    



