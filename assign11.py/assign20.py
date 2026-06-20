# Problem Statement
# An online payment company wants to build a secure digital wallet system.
class DigitalWallet:
    def __init__(self,username,balance,password):
        self.username = username
        self.__balance = 20000
        self.__password = password
    def deposit(self,amount):
        self.__balance +=amount
    def withdraw(self,password,amount):
         if password == self.__balance:
             self.__balance -=amount
             
         else:
             print("sufficient funds") 
        

        