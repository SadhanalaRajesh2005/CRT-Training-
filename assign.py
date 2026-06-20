#binary stair pattern
# n = int(input())
# for i in range(1,6):
#     for j in range(i):
#         print("*", end = " ")
#     print()


 
# n = int(input())
# for i in range(1,n+1) :
#     for j in range(i ):
#         if j % 2 == 0:

#          print(1,end=" ")
#         else :
#            print(0,end=" ")
#     print()




n = int(input())
for i in range(1,n+1):
    if i % 2 == 0 :
        for j in range (i,0,-1):
            print(j,end=" ")
    else:
            for j in range(1,i+1):
              print(j,end =" ")
        
        

    print()





    