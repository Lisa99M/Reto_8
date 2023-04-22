# Challenge_8
This is a repo about loops using for. In English, so the teacher can respect me a little bit more. 

1. Print a list with the numbers from 1 to 100, each one with its respective square. 
```
#Code:
for i in range (1,101):
    c = i**2
    print(i, c)
```
2. Print a list with the odd numbers from 1 up to 999, followed by another list with the even numbers from 2 up to 1000.
```
#Code
for i in range (1, 1000):
    if i%2 != 0:
        print(i)
for i in range (2, 1001):
    if i%2 == 0:
         print(i)
 ```

3. Print the even numbers that are less than or equal to a natural given number n ≥ 2, in descending order up to 2. 
```
#Code:
n: int
n = int(input("Input the number that is more than or iqual to 2"))
if n < 2:
    print("Invalid value")
else:
    print("Even numbers in descending order from " + str(n) + " to 2")
    for i in range(n,1, -1):
        if i%2 == 0:
            print(str(i))
```

4. Print the numbers from one to a given natural number (n), each with its respective factorial.
```
#Code:
fact: int = 1
n: int
n = int(input("Input value of n"))
print("Factorials from 1 up to " + str(n))
for i in range (1,n+1):
    fact *= i 
    print(i,fact)   
```

5. Calculate the value of 2 to the power n using for loops. 
```
#Code:
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
```
6. Read a natural number n and read another real data type. Calculate x^n using for loops. 
```
#Code:
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
```

7. Design a program that displays the multiplication tables from 1 to 9. 
```
#Code
n: int
multiplication: int
print("Multiplication tables from 1 to 9:")
for n in range(1,10):
    for i in range(1, 11):
        multiplication = n*i
        print(str(n) + "*" + str(i) + " = " + str(multiplication))
```
8. Design a function that finds an approximation of the exponential function around 0 for any (real) value of x, using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation. 
```
#Code
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
```
9. Design a function that allows calculating an approximation of the sine function around 0 for any value of x (real), using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation.
```
#Code
import math
def approximation_sine(x:float)-> float:
    summation = 0
    for i in range (0,n):
        summation += math.pow(-1,i)*((math.pow(x,(2*i)+1))/math.factorial((2*i)+1))
    return summation

if __name__ == "__main__":
 x = float(input("Input value of x"))
 n = int(input("Input value of the Maclaurin series term"))
 summation = approximation_sine(x)
  
print("Result using created funtion:"+ str(summation))
print("Result using function imported from math:"+ str(math.sin(x))) 
difference = math.atan(x) - summation
print("The difference between the actual value and the approximation is: " + str(difference))

#For the series approximations determine at which n value less than 0.1% error is obtained.
if abs(difference) > 0.1:
    print("There are not enugh terms for an error less than 0.1 percent" + str(n))
else: 
   print("The error is less than 0.1 percent with term" + str(n))
```
10. Design a function that allows calculating an approximation of the arctangent function around 0 for any value of x in the range [-1, 1], using the first n terms of the Maclaurin series. Displays the difference between the actual value and the approximation.
```
#Code
import math
x: float
x = float(input("Input value of x in range [-1,1]"))
if x < -1 or x > 1:
    print("Invalid value")
elif -1 <= x <= 1:
    def arctangent_function(x:float) -> float:
        summation = 0
        for i in range (0,n):
            summation += math.pow(-1,i)*(math.pow(x,(2*i+1))/(2*i+1))
        return summation

if __name__ == "__main__":
 x = x
 n = int(input("Input value of the Maclaurin series term"))
 summation = arctangent_function(x)
 
print("Result using created funtion:"+ str(summation))
print("Result using function imported from math:"+ str(math.atan(x))) 
difference = math.atan(x) - summation
print("The difference between the actual value and the approximation is: " + str(difference))

#For the series approximations determine at which n value less than 0.1% error is obtained.
if abs(difference) > 0.1:
    print("There are not enugh terms for an error less than 0.1 percent" + str(n))
else: 
   print("The error is less than 0.1 percent with term" + str(n))
```
