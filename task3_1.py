def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
a=input("ENTER A NUMBER ")
f=factorial(int(a))
print("factorial of",a,"is",f)

