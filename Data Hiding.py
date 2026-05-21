class Parent:
    def __init__(self, d):
        self._data = d

    def show(self):
        print(self._data)

class Child(Parent):
    def __init__(self, d):
        super().__init__(d)

    def display(self):
        print(self._data)

c= Child(25)
c.show()
c.display()