# You are allowed to remove at most one character from the string. Determine
# whether the message can become valid.
str = input("enter the string:")
left = 0
right =(len(str)-1)
while left < right:
   if str[left] != str[right]:
    False
    left +=1
    right -=1
True   
print("yes")

