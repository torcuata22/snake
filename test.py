# file = open("my_file.txt") #opens the file and creates the variable
# contents = file.read() #allows me to read the file
# print(contents)
# file.close() #open files take up resources (think of tabs open in browser), close files for best performance

#using WITH keyword:

#with open("my_file.txt") as file:
    # contents = file.read()
    # print(contents)

#with open("my_file.txt", mode = "a") as file:    #mode = a, appends and mode = w overwrites everything
    #contents = file.write("This is new, appended text.")

with open("new_file.txt", mode = "w") as nf: #only works for write mode
    nf.write("This is a brand new file")    
