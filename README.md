# Finding-Square-Roots
# This code (Python) will find the square root of any number
original=float(input("Input any number and I shall find the square root: "))
half=original/2
while half*half != original:
    closer_to_sqr = (half+original/half)/2
    half = closer_to_sqr
print(half, "is the square route")
