original=float(input("Input any number and I shall find the square root: "))
half=original/2
sqrt=1
while sqrt**2 < original:
    sqrt=sqrt+1
if sqrt**2==original:
    print(sqrt, "is the square route")
else:
    while half**2!=original:
        closer_to_sqr = (half+original/half)/2
        half=closer_to_sqr
        if (half*closer_to_sqr-original)**2<0.0000000000001:
            print("The square root of", original, "is about", half)
            break
