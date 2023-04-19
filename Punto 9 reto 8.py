#Design a function that allows calculating an approximation of the sine function around 0 for any value of x (real), using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation. Code:
import math
x:float
x = float(input("Input value of x"))
n: int
n = int(input("Input value of the Maclaurin series term"))

def approximation_sine(x):
    summation = 0
    for i in range (0,n):
        summation += math.pow(-1,i)*((math.pow(x,(2*i)+1))/math.factorial((2*i)+1))
    return summation
print("Result using created funtion:"+ str(approximation_sine(x)))
print("Result using function imported from math:"+ str(math.sin(x))) 
difference = math.atan(x) - approximation_sine(x)
print("The difference between the actual value and the approximation is: " + str(difference))