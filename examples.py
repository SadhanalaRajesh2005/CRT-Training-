# n =input("enter the string:")
# result =""
# for char in n:
#    if (char >='a' and char <='z') or (char >='A' and char <='Z'):
#       result += char
# print(result)   

# remove spaces without using strip

# n =input("enter the string:")
# result =""
# for char in n:
#     if char != "":
#         result += char
# print(result)

# n = input("enter the string:")
# result =""
# for char in n:
#     if char not in "(),[],{}":
#         result += char
# print(result)




# n = input("enter the string:")
# result = 0
# for char in n:
#     if char.isdigit():
#         result += int(char)
# print(result)


# capitalise the first and last charcter of word
# n =input("enter the string:")

# result =""
# words = n.split()
# for word in words:
#     if len(word) > 1:
#      result += word[0].upper() + word[1:-1] + word[-1].upper() + " "

     
#     else:
#         result += word.upper()
       
    

# print(result)

# check in anagram:

n1 = "silent"
n2 = "listen"
if sorted(n1) == sorted(n2):
    print("string is anagram")
else:
    print("not a string anagram")



