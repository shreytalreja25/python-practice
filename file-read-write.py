# import random

# f = open("Names.txt","r")
# f_content = f.read()
# # print(f_content)

# f_content_list = f_content.split("\n")

# # print(f_content_list)

# print(random.choice(f_content_list))
# f.close()

import random
f_name = input('Type the file name : ')
f = open(f_name,mode = "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))