def main():
    #Open a file for writing and create it if it doesn't exist
    #f = open("textfile.txt", "w+")

    #open the file for appending text to the end

    #write some lines of data to the file
    #for i in range(10):
        #f.write("This is line " + str(i) + "\r\n")

     #close the file when done
    #f.close()

    #Open the file for appending text to the end
    #f = open("textfile.txt", "a")



    #for i in range(10):
        #f.write("This is line " + str(i) + "\r\n")


    #open file for reading
    f= open("textfile.txt","r")

    #open the file back up and read the contents
    if f.mode == 'r':
        #contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)
        #print(contents)


if __name__ == "__main__":
    main()

    
        
