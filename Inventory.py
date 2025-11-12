from collections import Counter
inventory = Counter(apple=50, mango=100, banana=65, orange=80)

def update_inventory(order):
    inventory.subtract(order)

order = Counter(apple=15, banana=23, orange=20)
update_inventory(order)
print(inventory)