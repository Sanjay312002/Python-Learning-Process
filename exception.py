try:
    a = 10
    b = 0
    result = a / b
    print(result)
except:
    print("Something went wrong")


try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Denominator cannot be zero")



class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance -= withdraw
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print(e)