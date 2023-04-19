#Print the numbers from one to a given natural number (n), each with its respective factorial.Code:

fact: int = 1
n: int
n = int(input("Input value of n"))
print("Factorials from 1 up to " + str(n))
for i in range (1,n+1):
    fact *= i 
    print(i,fact)   




