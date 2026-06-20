# arr =[2,4,7,4,3]
# n =len(arr)
# # create prefix array
# prefix =[0]*n
# # [0,0,0,0,0]
# prefix[0] = arr[0]
# # [2,0,0,0,0]
# # build the prefix sum
# for i in range(1,n):
#     prefix[i] = prefix[i-1]+arr[i]
# print(prefix)


# l =1
# r = 3
# #range sum calculate
# if l == 0:
#     answer = prefix[r]
# else:
#     answer = prefix[r] - prefix[i - 1]
# print(answer)


# find the multiple range quaries

arr =[1,4,7,4,3]
n =len(arr)
# create prefix array
prefix =[0]*n
# [0,0,0,0,0]
prefix[0] = arr[0]
# [2,0,0,0,0]
# build the prefix sum
for i in range(1,n):
    prefix[i] = prefix[i-1]+arr[i]
print(prefix)


quaries =[(1,4),(2,5),(0,3)]
for l,r in quaries:
#range sum calculate
   if l == 0:
    answer = prefix[r]
else:
    answer = prefix[r] - prefix[l - 1]
print(answer)