# n =int(input())
# a =list(map(int, input().split()))
# k =int(input())

# window_sum = sum(a[:k])
# max_sum = window_sum
# for i in range(k,n):
#     window_sum = window_sum - a[i-k] +a[i]
#     if window_sum > max_sum:
#         max_sum = window_sum
# print(max_sum)



# n =int(input())
# a =list(map(int, input().split()))
# target =33
# left =0
# current_sum =0
# for right in range(len(a)):
#     current_sum = current_sum + a[right]
#     while current_sum > target:
#         current_sum = current_sum - a[left]
#         left = left +1


#     if current_sum == target:
#         print(a[left:right+1])
#     break


# n =int(input())
# a =list(map(int, input().split()))
# left = 0
# max_lenth= 0

# for i in range(len(a)):
#     seen = set()
#     for j in range(i,len(a)):
#         if a[j] in seen:
#             break
#         seen.add(a[j])
#     max_lenth = max(max_lenth,j-i+1)
# print(max_lenth)
    
    




    
