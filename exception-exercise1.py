items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)

except IndexError as e:
    print(e, "Something went wrong")

except Exception as e:
    print("Something went wrong " , e)


try:
    with open('file_does_not_exist.txt','r') as file:
        print(file.read())

except Exception as e:
    print("File doesnt exist...",e)


try:
    with open('filename.txt','r') as file:
        print(file.read())

except Exception as e:
    print(e)