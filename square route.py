tryagain="start"
while tryagain=="yes" or "start":
    tryagain="start"
    original=input("Input any number and I will find the square root: ")
    sqrt=1
    inverted_original=original*-1
    original=float(original)
    while abs(sqrt**2) < abs(original):
            sqrt=sqrt+1
    if sqrt**2==abs(original):
        if original < 0:
            print("The square root is imaginary", sqrt)
        else:
            print("The square route is", sqrt)
    elif original>0:
        while sqrt**2 != original:
            sqrt = (sqrt+abs(original)/sqrt)/2
            if abs(sqrt**2-original) < 0.0001:
                print("The square root of", original, "is about", sqrt)
                break
    else:
        while sqrt**2!=inverted_original:
            sqrt = (sqrt+abs(original)/sqrt)/2
            if abs(sqrt**2 - inverted_original)<0.0001:
                print("The square root of", original, "is about imaginary", sqrt)
                break
    while tryagain != "yes":
        tryagain=input("Type 'yes' to continue or 'no' to end the program: ")
        if tryagain== "no":
            break
    if tryagain=="no":
        break
