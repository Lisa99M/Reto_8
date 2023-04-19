#Design a function that allows calculating an approximation of the arctangent function around 0 for any value of x in range [-1, 1], using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation. Code
import math
x: int
x = int(input("Input value of x in range [-1,1]"))
if x < -1 or x > 1:
    print("Invalid valueo")
elif -1 <= x <= 1:
    def arctangent_function(x):
        summation = 0
        for i in range (-1,2,1):
            summation += math.pow(-1,i)*((math.pow(x,(2*i)+1))/(2*i)+1)
        return summation
print("Result using created funtion:"+ str(arctangent_function(x)))
print("Result using function imported from math:"+ str(math.atan(x))) 
difference = math.atan(x) - arctangent_function(x)
print("The difference between the actual value and the approximation is: " + str(difference))


