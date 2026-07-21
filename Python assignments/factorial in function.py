def factori(a):
    fact = 1

    for i in range(1, a + 1):
        fact *=i

    print("Factorial =", fact)


a = int(input("Enter the number: "))
factori(a)
    