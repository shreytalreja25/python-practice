# Slice function is used to search a particular phrase from a string
# str[start:stop:step]

# Using slice function to reverse a string
trial = "ABCDEF"
new_trial = trial[::-1]
print(new_trial)

# Using recursion to reverse a string
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = "QWERTY"
print(string_reverse(str))
