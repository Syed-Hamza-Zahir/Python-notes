import Abstraction
import Abstraction2

cust = Abstraction.Customer()
cust._firstname = "Syed"
cust._lastname = "Zahir"

print(cust._lastname)
cust.fullname()

cust._lastname = "Shah" # Problem with encapsulation here, data can be changed by user
print(cust.lastname)

person = Abstraction2.Student('Syed', 'Zahir')
print(person.firstname)
