List=['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
letter=input("Enter letter: ")

for x in List:
    if x.startswith(letter):
        print(x)