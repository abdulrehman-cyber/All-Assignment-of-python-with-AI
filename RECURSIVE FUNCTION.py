def sam(n):
     if n==0:
        return
     print(n)    
     sam(n-1)
n=int(input("Enter the n value = "))
sam(n)