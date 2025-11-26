def decorator(f):
    def message():
        print('*'*10)
        f()
        print('*'*10)

    return message

@decorator

def display():
    print('Welcome')

display()