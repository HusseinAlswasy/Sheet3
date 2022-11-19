                                            #video

N = int(input())
M = input().split()

i=0

max1=M[i]
max2=M[i]

for i in range(N):
    if M[i]>max1: #10 20 15   #15>20
        max2=max1             #10
        max1=M[i]             #20
    elif M[i]>max2:  # 15 > 10
        max2=M[i]
        


print(int(max1),int(max2))   


                                        #4- Replacment
# N = int(input())
# A = input().split()
# i = 0

# for i in range(N):
#     if (int(A[i]) > 0):
#         print(1,end=' ')
#     elif(int(A[i])==0):
#         print(0,end=' ')  
#     else:
#         print(2,end=' ')      



 

                                    
    
                                     

    











