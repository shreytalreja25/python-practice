try:
    with open("sample/newfile.txt",mode="a") as file:
        file.write("This is a new file and text is written from the program \n")
except FileNotFoundError as e:
    print("Error >>> ",e)