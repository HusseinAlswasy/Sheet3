                                    #6 -Position in Array
N = int(input())
M = input().split()

for i in range(N):
    if(int(M[i])<=10):
        print("A["+str(i)+"] = "+M[i])