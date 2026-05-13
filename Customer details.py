class Customer:
    def __init__(self, name, phoneno):
        self.name = name
        self.phno = phoneno

    def get_name(self):
        return self.name
    
    def get_phoneno(self):
        return self.phno
    
    def set_phoneno(self,ph):
        self.phno = ph

c1 = Customer('Swarali', 9913148640)
print('Name: ', c1.get_name())
print('Phone no: ', c1.get_phoneno())

c1.set_phoneno(9428968144)

print('')
print('Name: ', c1.get_name())
print('Phone no: ', c1.get_phoneno())