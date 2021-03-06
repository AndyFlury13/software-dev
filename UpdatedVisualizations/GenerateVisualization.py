import csv
import sys
import shutil
import fileinput
import os
import os.path

arg_list = sys.argv
print(arg_list)
articleID = arg_list[1]

shutil.copy("Visualization.html", os.getcwd() + "/TestBed")
curName = "TestBed/Visualization" + articleID + ".html"
os.rename("TestBed/Visualization.html", curName)
shutil.move(curName, os.getcwd())
curName = "Visualization" + articleID + ".html"

text = ""

#with open(articleID + "SSSArticle.txt", encoding='utf-8') as file:
#    text = file.read()

with fileinput.FileInput(curName, inplace=True) as file:
    for line in file:
        print(line.replace("ARTICLEIDHERE", articleID, 1), end='')

#with fileinput.FileInput(curName, inplace=True) as file:
#    for line in file:
#        print(line.replace("ARTICLETEXTHERE", text, 1), end='')

cmdString = "aws s3 mv "+ curName + " s3://publiceditor.io/Articles" + curName + " --acl public-read-write"
os.system(cmdString)
