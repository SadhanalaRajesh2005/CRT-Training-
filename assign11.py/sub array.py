# n =int(input())
# a =list(map(int, input().split()))
# k = int(input())
# max_sum = 0
# for i in range(len(a)-k+1):
#     current_sum = 0
#     for  j in range(i,i+k):
#         current_sum = max_sum+current_sum
#         max_sum = current_sum
#     print(max_sum)



# find the first condition subarray whose sum equals to the target
# continues subarray
# 1.elements should be adjacent
# 2.elements should not skipped
# n =int(input())
# a =list(map(int, input().split()))
# found = False
# target = 33


# for i in range(len(a)):
#     current_sum = 0
    
#     for j in range(i,len(a)):
#         current_sum = current_sum + a[j]
#         if current_sum == target:
#             print(a[i:j+1])
#             found = True

#             break

# if found:
#         target = current_sum


# problem3:
# find the longest cointinues subarray
# that contians no repeating elements/


n =int(input())
a =list(map(int, input().split()))
left = 0
max_len = 0
seen =set()

for i in range(len(a)):
    while a[i] in seen:
      seen.remove(a[left])
      left = left + 1
    seen.add(a[i])
    max_len =max(max_len,i-left+1)
print(max_len)
    

   



