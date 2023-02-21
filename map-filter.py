menu = ["espresso","mocha","latte","cappuccino","americano","cortada"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    
map_coffee = map(find_coffee,menu)
print(map_coffee)

for i in map_coffee:
    print(i)

filter_coffee = filter(find_coffee,menu)
print(filter_coffee)

for i in filter_coffee:
    print(i)