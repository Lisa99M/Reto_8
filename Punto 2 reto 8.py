#Print a list with the odd numbers from 1 up to 999, followed by another list with the even numbers from 2 up to 1000. Code:
for i in range (1, 1000):
    if i%2 != 0:
        print(i)
for i in range (2, 1001):
    if i%2 == 0:
         print(i)