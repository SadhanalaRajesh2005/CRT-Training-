# n =int(input())
# a =list(map(int, input().split()))
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)


# count of even numbers
n =int(input())
a =list(map(int, input().split()))
count = 0
for i in a:
    if i % 2 !=0:
        count +=1
print(count)
