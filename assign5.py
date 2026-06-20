# n =int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(i):
#             print("*",end=" ")
#     print()


# hollowup :

        
# N = int(input())

# for i in range(N, 0, -1):           # N to 1 rows, inverted kabatti
#     # 1. Left side spaces
#     for j in range(N - i):
#         print(" ", end="")
    
#     # 2. Stars + hollow spaces
#     for k in range(1, i + 1):
#         if i == N or k == 1 or k == i:   # First row, 1st column, last column
#             print("*", end=" ")
#         else:                            # Lopala hollow
#             print(" ", end=" ")
#     print()


# N = int(input())

# for i in range(1, N + 1):          
    
#     for j in range(N - i):          
#         print(" ", end="")
    
#     # 2. Print stars + hollow part
#     for k in range(1, i + 1):       
#         if i == N or k == 1 or k == i:   
#             print("*", end=" ")
#         else:                            
#             print(" ", end=" ")
#     print()                         



