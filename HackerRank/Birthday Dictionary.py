bday={'Swarali':'01/03/2003', 'Anuj':'28/08/2002', 'RDJ':'04/04/1965', 'Mark':'16/06/2004'}
person=input("Enter name: ")

if person in bday:
    print(person, bday[person])
    #print("Mr./Ms. {} was born on {}".format(person, bday[person]))
else:
    print("No record found")
