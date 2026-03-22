def Fib(n,k):
 return n if n<=1 else Fib(n-1,k) + k*Fib(n-2,k)
n=int(input("Enter your n:"))
k=int(input("Enter your K:"))
print(Fib(n,k))