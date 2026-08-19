N=int(input()) 
sieve=[True]*(N+1); sieve[0]=sieve[1]=False 
i=2 
while i*i<=N: 
    if sieve[i]: 
        for j in range(i*i,N+1,i): sieve[j]=False 
    i+=1 
print(*(i for i in range(N+1) if sieve[i]))