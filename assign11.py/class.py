# name = input("enter name:")
# print("hello",name,sep=" ,",end = "!")


# num = input("enter a num:")
# print("you entered:",num)



# name = input("enter the name:")
# print("hello",name)

# list in total numbers
# n = int(input())
# a =list(map(int, input().split()))
# total = 0
# for i in a:
#     total = total + i
# print(total)


# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# 1 nunchi user number varaku even numbers matrame print cheyyali
# n = int(input())
# a = list(map(int, input().split()))
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count +=2
#         print(count)


# String Length
# n =input("enter the input:")
# print(len(n))
    
# n =input("enter the name:")
# rev = n
# print(rev[::-1])

# n =input("enter the vowel:")
# vowels ="a,e,i,o,u"
# count = 0
# for i in n:
#     if i in vowels:
#        count +=1
# print(count)


# 

# check the biggest number in list
# a =input("enter the number:")
# b =input("enter the number:")
# c =input("enter the number:")
# biggest = a
# if biggest > b and biggest > c:
#     print(a)
# elif b > c and b > a:
#     print(b)
# else:
#     print(c)



# n = int(input("enter the number:"))
# if n == 0:
#     print("zero")
# elif n > 0:
#     print("positive")
# else:
#     print("negative")



# n =int(input())
# a = list(map(int, input().split()))
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count +=1
# print("even:",count)
# if i % 1 == 0:
#         count +=1
# print("odd:",count)



# n = int(input())
# a = list(map(int, input().split()))
# for i in a:
#     if i >= 35:
#         print("pass")
#     else:
#         print("fail")



# n =int(input())
# while n > 0:
#     digit = n % 10
#     n = n // 10
#     print(digit)

# palindrome or not check 
# n = int(input())
# original = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if rev == original:
#     print("palindrome")
# else:
#     print("not a palindrome")

# check whether the armstrong

# n = int(input())
# original = n
# power =len(str(n))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit**power
#     n = n // 10
# if original == sum:
#     print("armstrong")
# else:
#     print("not a armstrong")


# n =int(input())
# original = n
# sum = 0

# while n > 0:
#     digit = n % 10
#     fact = 1
#     for i in range(1,digit+1):
#       fact *= i
#     sum = sum + fact
#     n = n // 10
# if original == sum:
#     print("strong number")
# else:
#     print("not a strong number")
    

# for n in range(100, 501):
   

#    original = n
#    sum = 0
#    temp = n
   
#    while temp > 0:
#       digit = temp % 10
      
#       fact = 1
#       for i in range(1, digit+1):
#         fact *=i
#       sum += fact
#       temp = temp // 10
#    if original == sum:
#         print("strong number",n)
      
    

