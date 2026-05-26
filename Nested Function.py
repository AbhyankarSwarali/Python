def Outer():

    def Inner():
        print('Inner')

    print('Outer')
    Inner()


Outer()