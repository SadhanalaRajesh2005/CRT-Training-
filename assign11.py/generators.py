# simply generators work is same as 
# produces values one at a Time
# only when it is needed
# saves memory
# it uses in generator yield keyword
# yeild pauses the function

# return :ends the function
# ex 
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# x = numbers()
# print(x)
# # access the numbers
# print(next(x))
# print(next(x))

# def test():
#     yield 1
#     yield 2
# x = test()
# print(next(x))
# return only one value by 1 and End
# yield key word multiple value 

# def even_numbers(limit):
#     num = 2
#     while num <= limit:
#         yield num
#         num +=2
# x = even_numbers(10)
# for i in x:
#     print(i)


# decorators:
# adds the extra functionality
# without changing 
# def greet():
#     print("hello students")
# x =greet
# x()




