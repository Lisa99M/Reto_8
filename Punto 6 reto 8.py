#Design a program that displays the multiplication tables from 1 to 9. Code:
n: int
multiplication: int
print("Multiplication tables from 1 to 9:")
for n in range(1,10):
    for i in range(1, 11):
        multiplication = n*i
        print(str(n) + "*" + str(i) + " = " + str(multiplication))
