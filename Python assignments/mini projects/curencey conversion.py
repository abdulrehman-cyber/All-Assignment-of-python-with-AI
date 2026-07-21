def converter(usd_val):
    pkr_val= usd_val* 278
    print(usd_val,"USD=",pkr_val,"PKR")
    return pkr_val
usd_val= int(input("Enter the dallor amount ="))
converter(usd_val)