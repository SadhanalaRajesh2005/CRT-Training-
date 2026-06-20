# num = {1,2,3,4,5}
# num.add(10)
# print(num)
# num.remove(2)
# print(num)
# print(num.discard(10))
# print(num)
# num.pop()
# print(num)
# num.clear()
# print(20 in num)

# 1.UnicodeEncodeError |
# 2.intersection &
# 3.diffrence -
# symmetric difference a^b  not common elements in set


# a = {1,2,3}
# b  ={2,3,6}
# # print(a|b)
# # # print(a.intersection(b))
# # # print( a & b)
# # print( a - b)
# print(a ^ b)

# subset and superset
# a = {1,2,3}
# b  ={1,2,3,4}
# print(a.issubset(b))
# print(b.issuperset(a))


# frozenset  immutable version in set
# cannot add 
# cannot delete

# fs = frozenset([1,2,3,4,5])
# print(fs)


# problem1
# find the longest length of consecutive sequence

nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
longest = 0
for i in s:
    if i - 1 not in s: 
      length =1
      while i + length in s: 
        length += 1
    longest = max(longest, length)
print(longest)




 