#Read a natural number n, and another real data type x. Calculate x to the n power using for loops. Code:
x: float
n: int
resultado:float
x = float(input("Input value of x"))
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