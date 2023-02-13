# Scopes in Python are : Local Scope, Enclosing Scope , Global Scope , Built-in Scope

# GLOBAL SCOPE

global_variable = 10

def scoping():
    local_variable = 20
    print("We can access ", global_variable)

scoping()

# LOCAL SCOPE

# print("We cant access ", local_variable)