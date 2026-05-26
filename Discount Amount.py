amount = float(input("Enter bill amount: "))

if amount <= 0:
    print("Invalid value")
elif amount <= 1000:
    discount = amount * 10 / 100
    print('Discount = ',discount)
elif 1000 < amount <= 5000:
    discount = amount * 20 / 100
    print('Discount = ',discount)
elif 5000 < amount <= 10000:
    discount = amount * 30 / 100
    print('Discount = ',discount)
else:
    discount = amount * 50 / 100
    print('Discount = ',discount)

payable_amount = amount - discount

print("Payable bill: ", payable_amount)