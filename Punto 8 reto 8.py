#Design a function that finds an approximation of the exponential function around 0 for any (real) value of x, using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation. Code
import math
n: int
n = (int(input(" Number of the term of Maclaurin series")))
x: float
x = (float(input("Real value to calculate the approximation of the exponential fucntion around 0")))
def exponential_function (x):
    summation = 0
    for i in range (0, n):
        summation += math.pow(x, i) / math.factorial(i)
    return summation
print("Result using created funtion:"+ str(exponential_function(x)))
print("Result using function imported from math:"+ str(math.exp(x))) 
difference = math.exp(x) - exponential_function(x)
print("The difference between the actual value and the approximation is: " + str(difference))
