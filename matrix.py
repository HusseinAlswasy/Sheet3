                                        #5- matrix

N = int(input())

A=[]
sum_main =0
sum_secondry=0

for i in range(N):
    A.append(input().split())
for j in range(N):
    sum_main= sum_main + int(A[j][j])
    sum_secondry= sum_secondry + int(A[j][N-1-j])
print(abs(sum_main-sum_secondry))