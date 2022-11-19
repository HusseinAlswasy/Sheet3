                                   #7- Replace MinMax
N = int(input())
M = input().split()   

i=0 

posmin =0
posmax =0

temp =0

min = M[i]
max = M[i]
for i in range(N):
    if int(M[i]) < int(min):
        min = M[i]   #5
        posmin = i #3
    elif int(M[i]) > int(max):
        max = M[i]   #30
        posmax = i #5
        

M[posmin] = max
M[posmax] = min

print(' '.join(M))  # 10 20 5 15 30   max=30,posmax=4  min=5,posmin=2
            # 10 20 30 15 5