original=float(input("Input any number and I shall find the square root: "))
half=original/2
sqrt=1
while abs(sqrt**2) < abs(original):
    sqrt=sqrt+1
if sqrt**2==abs(original):
    if original < 0:
        print("Imaginary", sqrt, "is the square root")
    else:
        print(sqrt, "is the square route")
else:
    while abs(half**2)!=abs(original):
        closer_to_sqr = (half+abs(original)/half)/2
        half=closer_to_sqr
        if (half*closer_to_sqr-abs(original))**2<0.0000000000001:
            if original < 0:
                print("The square root of", original, "is about imaginary", half)
                break
            else:
                print("The square root of", original, "is about", half)
                break
    
