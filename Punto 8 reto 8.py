#Design a function that finds an approximation of the exponential function around 0 for any (real) value of x, using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation. Code
import math
def exponential_function (x:float,n:int) -> float:
    for i in range (0, n):
        summation = 0
        summation += math.pow(x, i) / math.factorial(i)
    return summation


if __name__ == "__main__":
  n = (int(input(" Number of the term of Maclaurin series")))
  x = (float(input("Real value to calculate the approximation of the exponential fucntion around 0")))
  summation = exponential_function (x, n)
  
print("Result using created funtion:"+ str(summation))
print("Result using function imported from math:"+ str(math.exp(x))) 
difference = math.exp(x) - summation
print("The difference between the actual value and the approximation is: " + str(difference))

#For the series approximations determine at which n value less than 0.1% error is obtained.
if abs(difference) > 0.1:
    print("There are not enugh terms for an error less than 0.1 percent" + str(n))
else: 
   print("The error is less than 0.1 percent with term" + str(n))
