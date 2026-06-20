# n = int(input())
# claps = input().split()
# total = 0
# for i in range (n):
#     total = total + int(claps[i])

# average_claps = total / n
# print("totalclaps",total )
# print ("averagclaps", int(average_claps))

# problem 2 : mobile battery warning

# battery = int(input())
# usage = int(input())
# hours = 0
# while battery > 20 :
#     battery = battery - usage
    
#     hours = hours + 1
# print("hours",hours)
# print("bettery_left:",(battery))


#lucky bus ticket

# n = int(input())
# if n % 3 ==0 and n % 5 == 0 :
#     print("lucky ticket")
# else:
#     print(" not a lucky")

# 4 . water bottle tracker 
# n = int(input())
# usage_per_hour = int(input())
# hours = 0
# while water > 1:
#     water = water - usage_per_hour
#     hours = hours + 1
# print("hours",hours)
# print("water_intake",water)



# 5 . secret number door
# a = int(input())
# b = int(input())
# c = int(input())
# if a == 7 or b == 7 or c == 7 :
#     print ("door opened")
# else :
#     print("access denied")





# 6 . candy box entered
# n = int(input())
# for i in range(1 , n + 1) :
#    if i % 2 == 0 :
#       print(i , end =" ")

# 7: Skipping Broken Steps


# n = int(input())
# for i in range (1 , n +1) :
#         if i % 4 != 0:
#                 print(i, end =" ")

# n = int (input())
# i = 1


# while i <= n :
#    if i % 4 != 0 :


#     print (i , end=" ")
#    i = i + 1



# 8: Mini Shopping Bill


n = int(input())
prices = (map(int , input().split()))
total = 0
highest = 0
for  price in prices:
    total += price
    if price > highest :

        highest = price


print("total",total) 
print("highest",highest)


