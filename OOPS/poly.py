# compile time polymorphism

#Using *args 

class Calculator:
    def add(self,*numbers):
        return sum(numbers)

cal = Calculator()
print(cal.add(10,20))
print(cal.add(10,20,30))
print(cal.add(10,20,30,40))
print(cal.add(10,20,30,40,50))


#Run time polymorphism
#Method Overriding

class Payment:
    def pay(self):
        print("Payment")

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

class credit_card(Payment):
    def pay(self):
        print("Payment through Credit card")

class cash(Payment):
    def pay(self):
        print("Payment through cash")


def pay_process(payment):
    payment.pay()




pay_process(UPI())
pay_process(credit_card())
pay_process(cash())
