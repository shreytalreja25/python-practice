import os

def list_files(path):
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path,item)
            if os.path.isfile(item_path):
                print(item_path)
            elif os.path.isdir(item_path):
                list_files(item_path)
    except Exception as e:
        print("An error happened", e)

print(list_files(r"C:\Users\shrey\python-practice"))