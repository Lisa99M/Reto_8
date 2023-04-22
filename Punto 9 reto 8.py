#Design a function that allows calculating an approximation of the sine function around 0 for any value of x (real), using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation. Code:
import math
def approximation_sine(x:float,n:int)-> float:
    summation = 0
    for i in range (0,n):
        summation += math.pow(-1,i)*((math.pow(x,(2*i)+1))/math.factorial((2*i)+1))
    return summation

if __name__ == "__main__":
 x = float(input("Input value of x: "))
 n = int(input("Input value of the Maclaurin series term: "))
 summation = approximation_sine(x,n)
  
print("Result using created funtion: "+ str(summation))
print("Result using function imported from math: "+ str(math.sin(x))) 
difference = math.sin(x) - summation
print("The difference between the actual value and the approximation is: " + str(difference))

#For the series approximations determine at which n value less than 0.1% error is obtained.
if abs(difference) > 0.001:
    print("There are not enugh terms for an error less than 0.1 percent " + str(n))
else: 
   print("The error is less than 0.1 percent with term " + str(n))