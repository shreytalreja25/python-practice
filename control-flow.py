# Using conditional logic using if/else syntax

bill_total = int(input("Enter Bill Total : "))
discount_1 = 10
discount_2 = 20
# print(type(bill_total))
if bill_total > 100 and bill_total < 200:
    print("Bill greater than 100")
    bill_total = bill_total - discount_1
    discount = discount_1
elif bill_total>200:
    print("Bill greater than 200")
    bill_total = bill_total - discount_2
    discount = discount_2
else:
    discount = 0
    print("Bill is less than 100")

print("Total Bill : " + str(bill_total) + " Discount applied : " + str(discount))
