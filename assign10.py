# Rotate Array by K Positions
# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())
# for i in a:
    
#         if k == 0:
#           print(*a)
#         else:
#            rotated= a[-k:] + a[:-k]
# print(rotated)



# #2. Find Missing Number
# n =int(input())
# a =list(map(int, input().split()))
# expected_sum=n*(n+1) // 2
# actual_sum= sum(a)
# missing = expected_sum - actual_sum
# print(missing)


# 3.Maximum Difference Between Two Elements
# n = int(input())
# a = list(map(int, input().split()))

# min_val = a[0]
# max_diff = a[1] - a[0] 

# for i in range(1, n):
#     diff = a[i] 
    
#     if diff > max_diff:
#         max_diff = diff
    
#     if a[i] < min_val:
#         min_val = a[i] 

# print(max_diff)


# 4.Check if Array is Sorted
# n =int(input())
# a =list(map(int, input().split()))
# is_sorted= True
# for i in range(n-1):
#     if a[i] > a[i+1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("sorted")
# else:
#     print("not sorted")
