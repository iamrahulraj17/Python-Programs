def f(n):
    if (n<2):
        return 1
    else:
        return f(n-1)+f(n-2)
    
n = int(input("Enter a number:"))
print(f(n-2))
