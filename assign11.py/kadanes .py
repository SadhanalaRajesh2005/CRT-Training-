# kadanes alogorithm max sub array problems
# arr =[1 -2 ,3 -2 ,4]
# find the contigious sub array with max sum
# sub array:[1,-2,3] valid
# [-2,3] invalid
# subarrays    sum
# [2]          2
# [2,-1]       1
# [2,-1,3]      4
# [2,-1,3,-1]  2
# 1 -2 ,3 -2 ,4] 6


# kadanes alogorithm
# two Choices
# 1. continous sub array
# 2.start a new subarray


# current_sum = -5
# next_element = 10
# -5 + 10 = -5
# next =10

# current_sum = max(arr[i],current_sum[i])
# max_sum = max(max_sum,current_sum)


# arr = [2,-1,3,-2,4]
# current_sum = arr[0]
# max_sum = arr[0]
# for i in range(1,len(arr)):
#     # either continue with old subarray
#     # or stsrt a new sub arr
#     current_sum = max(arr[i],current_sum+arr[i])
#     max_sum = max(max_sum,current_sum)
# print(max_sum)




# arr = [-2,4,-1,5,-3,2]

# current_sum = arr[0]
# max_sum = arr[0]
# start= 0
# end = 0
# temp_start = 0

# for i in range(1,len(arr)):
  
#   if arr[i] > current_sum+arr[i]:
#     current_sum = arr[i]
# # NEW POSSIBLE Starting index
#     temp_start = i
#   else:
#     current_sum = current_sum+arr[i]
# # update the maximum
#     if current_sum > max_sum:
#       max_sum = current_sum
# #   save the index values
#       start = temp_start
#       end = i
# print(max_sum)
# print(start)
# print(end)
# print(arr[start:end+1])



    




    

