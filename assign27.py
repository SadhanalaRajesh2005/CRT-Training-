# # Parallel Marks Evaluation
# import threading
# from threading import Thread

# lock = threading.Lock() # print order marakunda kosam

# def evaluate_student(name, math, physics, chemistry):
#     total = math + physics + chemistry
#     avg = total / 3

#     result = "PASS" if avg >= 40 else "FAIL"

#     # Lock tho print cheyyadam valla output order clean ga osthundi
#     with lock:
#         print(f"{name} {total} {result}")

# # Input theeskundam
# N = int(input())
# threads = []

# for _ in range(N):
#     data = input().split()
#     name = data[0]
#     math = int(data[1])
#     physics = int(data[2])
#     chemistry = int(data[3])

#     # Prathi student ki oka thread
#     t = Thread(target=evaluate_student, args=(name, math, physics, chemistry))
#     threads.append(t)
#     t.start()

# # Main thread anni threads aipoyela wait chesthundi
# for t in threads:
#     t.join()

# print("Result Processing Completed")


# Thread Safe Bank Transaction:

# import threading
# from threading import Thread

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#         self.lock = threading.Lock()  # synchronization kosam

#     def withdraw(self, amount):
#         with self.lock:  # Lock teeskoni critical section start
#             if self.balance >= amount:
#                 self.balance -= amount
#                 print(f"{amount} withdrawn")
#             else:
#                 print("Insufficient Balance")

# def process_request(account, amount):
#     account.withdraw(amount)

# # Input
# B = int(input().strip())
# N = int(input().strip())
# withdrawals = [int(input().strip()) for _ in range(N)]

# account = BankAccount(B)
# threads = []

# # Prathi withdrawal ki oka thread
# for amt in withdrawals:
#     t = Thread(target=process_request, args=(account, amt))
#     threads.append(t)
#     t.start()

# # Main thread anni threads complete ayye varaku wait
# for t in threads:
#     t.join()

# print(f"Final Balance: {account.balance}")