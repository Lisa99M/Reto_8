#Print the even numbers that are less than or equal to a natural given number n ≥ 2, in descending order up to 2. Code:
n: int
n = int(input("Input the number that is more than or iqual to 2"))
if n < 2:
    print("Invalid value")
else:
    print("Even numbers in descending order from " + str(n) + " to 2")
    for i in range(n,1, -1):
        if i%2 == 0:
            print(str(i))





