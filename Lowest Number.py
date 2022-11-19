                                #E. Lowest Number
N =int(input())
M=input().split()

i=0
min =M[i]
pos =1

for i in range(N):
    if M[i] < min:
        min = M[i]
        pos = i+1

print(min,pos)
                 