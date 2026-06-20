# Print numbers from 1 to 10.
# for i in range(1 , 11):
#     rev =i[::-1]
# print(rev)
# in reverse in 10 to 1:
# for i in range(10 , 0 ,-1):
#     print(i)

# Print the multiplication table of a given number
# n =int(input())
# for i in range (1 , 11):
#   print(f"{n} * {i} = {n * i}")
    
# Count the number of digits in a number
n =int(input("enter the numbers:"))
a =abs(n)
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n = n // 10
        count +=1
print(count)