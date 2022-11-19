

                                             #2- search
N =int(input())
A = input().split()
M = int(input())

i=0
found = False
for i in range(len(A)):
    if(int(A[i])==M):
        print(i)
        found = True
        break
if(found == False):
    print(-1)
