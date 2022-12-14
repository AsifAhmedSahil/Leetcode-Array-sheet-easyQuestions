def Fibonacci(n):
    seen = {0:0,1:1}
    
    for i in range(2,n+1):
        seen[i] = seen[i-1] + seen[i-2]
    return seen[n]

print(Fibonacci(6))

# this is best for timing 
