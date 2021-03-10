import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
    #print the name of the os
    print(os.name)

    #check fo item existence and type
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))

    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name " + str(path.split(path.realpath("textfile.txt"))))

    #Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)

    #a different format for displaying the time
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    #Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

    print("It has been " + str(td) + "since the file was last modified")
    print("Or, " + str(td.total_seconds()) + "seconds")

    
if __name__== "__main__":
    main()
