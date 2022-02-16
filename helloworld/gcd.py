# print statement

print("Hello world")

# find the greatest common denominator (GCD) of two integers.
# example GCD of 20 and 8 is 4

# 1. for two integers a and b, where a > b, divide by b.
# 2. if the remainder, r, is 0 then stop, you found it. GCD is b.
# 3. Otherwise, set a to b, b to r and repeat at step 1 until r is 0
def gcd(a,b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a


print(gcd(60,96))  # should be 12
print(gcd(20,8))