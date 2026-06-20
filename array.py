# n = int(input())
# a =list(map(int, input().split()))

# for i in range(1,n):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")


# n = int(input())
# a =list(map(int, input().split()))
# count =0
# for i in (a):
#     if i % 3 == 0:
#         count += 1
#     print(count)


# n =int(input()) 
# a =list(map(int, input().split()))

# for i in a:
#     difference = abs(a[0]-a[-1])
#     print(difference)


# n =int(input()) 
# a =list(map(int, input().split()))

# for i in a:
#     if a.count(i) == 1:
#         print(i,end=" ")

# list the values -ve ,+ve and starting numbers in -ve numbers
# n =int(input()) 
# a =list(map(int, input().split()))
# N = []
# P = []
# for i in a:
#     if i < 0:
#         N.append(i)
#     else:
#         P.append(i)
# result=N+P
# print(result)

# frequency of the elements
# n =int(input()) 
# a =list(map(int, input().split()))
# freq ={}

# for i in a:
#     if i in freq:
#         freq[i] = freq[i]+1
#     else:
#         freq[i]=1
# print(freq,end="")


# adding of target numbers
# 2 pointers
# target =int(input())
# a =list(map(int, input().split()))

# i = 0
# j = (len(a)-1)
# while i < j:
#     current_sum=a[i]+a[j]
#     if current_sum == target:
#         print("pair is found:",a[i],a[j])
#         break
#     elif current_sum < target:
#         i +=1
#     else:
#         j -=1

# reverse of number
# reverse = int(input())
# a =list(map(int, input().split()))
# i = 0
# j = (len(a)-1)
# while i < j:
#     a[i],a[j] = a[j],a[i]
#     i +=1
#     j -=1
#     print(a)



# a =list(map(int, input().split()))
# i = 0 
# j = (len(a)-1)
# while i < j:
#     if a[i] != a[j]:
#         print(" not a palindrome")
#         break
#     else:
#         print("palindrome")
#         i +=1
#         i -=1



n =int(input())
a =list(map(int, input().split()))
i =0
for j in range(len(a)):
    if a[j] !=0:
        a[i],a[j]=a[j],a[i]

    i +=1
    print(a)




    







 





    
        

