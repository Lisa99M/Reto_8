# Calculate the value of 2 to the power n using for loops. Code:
x: int = 2
n: int
result:int
n = int(input("Input value of n, exponent of the power"))
result = x
if n == 0:
    result = 1
    print(str(x) + " to the power " + str(n) + " is equal to: " + str(result))
elif n == 1:
    print(str(x) + " to the power " + str(n) + " is equal to: " + str(result))
for i in range(1,n):
    result=result*x
print(str(x) + " to the power " + str(n) + " is equal to: " + str(result))
