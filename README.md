original=float(input("Input any number and I shall find the square root: "))
sqrt=1
inverted_original=original*-1
while abs(sqrt**2) < abs(original):
    sqrt=sqrt+1
if sqrt**2==abs(original):
    if original < 0:
        print("The square root is imaginary", sqrt)
    else:
        print("The square route is", sqrt)
elif original>0:
    while sqrt**2 != original:
        closer_to_sqr = (sqrt+abs(original)/sqrt)/2
        sqrt=closer_to_sqr
        if abs(sqrt**2-original) < 0.0000000000001:
                print("The square root of", original, "is about", sqrt)
                break
else:
    while sqrt**2!=inverted_original:
               closer_to_sqr = (sqrt+abs(original)/sqrt)/2
               sqrt=closer_to_sqr
               if abs(sqrt**2 - inverted_original)<0.00000000001:
                   print("The square root of", original, "is about imaginary", sqrt)
                   break
