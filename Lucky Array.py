                                    #3- Lucky Array

N=int(input())
A=input().split()
i=0
j=0
min=A[i]
num=0
for i in range(N):
    if int(A[i])<int(min):
        min=A[i]
for j in range(N):
    if(A[j]==min):
        num+=1
if(num%2==0):
    print('Unlucky')
else:
    print('Lucky')