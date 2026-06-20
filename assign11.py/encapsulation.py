# class Bank:
#     def __init__(self):
#         self.balance = 10000
#     def deposit(self,amount):
#         self.balance +=amount

#     def show_balance(self):
#         print(self.balance)
# b1 = Bank()
# b1.deposit(5000)
# b1.show_balance()


# try to access the name mangling
# class Student:
#     def __init__(self):
#         self.__marks = 90
# s1 = Student()
# print(s1._Student__marks)


# bank :create bank account:
# class BankAccount:
#     def __init__(self):
#         self.__balance = 10000
#     def deposit(self,amount):
#          self.__balance +=amount 
#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -=amount
#         else:
#             print("insufficient funds")
#     def show_balance(self):
#         print(self.__balance)
# b1 = BankAccount()
# b1.deposit(10000)
# b1.withdraw(20000)
# b1.show_balance()
# print(b1._BankAccount__balance)




# task:create a bankaccount
# create getter for returning balance
# create setter for updating balance
class BankAccount:
    def __init__(self):
        self.__balance = 10000
    def get_balance(self,amount):
        return self.get_balance
    