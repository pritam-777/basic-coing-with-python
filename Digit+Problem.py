N,K = input().split()
change = '9'
N= list(N)
for i in range(int(K)):
    N[i]=change

print(''.join([str(i) for i in N]))