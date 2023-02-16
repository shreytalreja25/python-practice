with open('newfilealt.txt','r') as file:
    for x in file:
        print(x)

with open('newfilealt.txt','a') as file:
    file.write("\nAdd new lines to the end of the file \n")