

# # cyclic Iterator Sum
# def cyclic_sum(): 
#    t = int(input())  

# for i in range(t):
#     n, k = map(int, input().split()) 
#     arr = list(map(int, input().split()))  
    
#     total_sum = sum(arr)
#     full_cycles = k // n
#     remaining = k % n
    
#     result = total_sum * full_cycles + sum(arr[:remaining])
#     print(result)


# Generator Password Stream

# t = int(input())  

# for i in range(t):
#     s = input().strip()  # string S
#     k = int(input())     # password length K
    
#     n = len(s)
#     full_rounds = k // n      # string motham enni sarlu repeat ayindi
#     remaining = k % n         # last lo migilina letters
    
#     password = s * full_rounds + s[:remaining]
#     print(password)