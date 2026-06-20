# longest substring without repeating characters:
# str = input()
# seen = set()
# left = 0
# max_len = 0
# for right in range(len(str)):
#     if str[right] in seen:
#         seen.remove(str[left])
#         left +=1
#     seen.add(str[right])
#     max_len = max(max_len,right-left+1)
# print(max_len)


# n =int(input())
# a =list(map(int, input().split()))
# left = 0
# right =len(a)-1
# while left < right:
#     mid =(left + right) // 2
#     if a[mid] < a[mid + 1]:
#         left = mid + 1
#     else:
#         right = mid
# print(left)

# a = 10
# b = 20
# c = 30
# bigger = a
# if bigger >= b and bigger >= c:
#     print("a")
# elif b >= c and b >= a:
#     print(b)
# else:
#     print(c)

# Find the larger of two numbers.
# a =int(input())
# b =int(input())
# if a > b:
#     print("a:",a)
# else:
#     print("b:",b)

# Check whether a year is a leap year.
# n =int(input())
# a =list(map(int, input().split()))
# for i in a:
#     if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
#        print("leapyear")
#     else:
#         print("non leapyear")



# n =int(input())
# marks = 55
# if n >= 90:
#     print("Grade A")
# elif n >= 80:
#     print("Grade B")
# elif n >= 70:
#     print("Grade C")
# elif n >= 60:
#     print("Grade D")
# elif  n >= marks:
#     print("pass")
# else:
#     print("fail")

# Check if a person is eligible to vote (age ≥ 18)
# n =int(input())
# age = 18
# if n >= 18 or n == 18:
#     print("eligible")
# else:
#     print("not eligible")


