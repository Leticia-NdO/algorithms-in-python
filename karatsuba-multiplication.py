# Explanation:
#   The Karatsuba multiplication algorithm is a fast multiplication algorithm that
# uses a divide-and-conquer approach to multiply two numbers. The basic idea behind
# the algorithm is to split the input numbers into smaller numbers, perform some 
# intermediate calculations, and then combine the results to obtain the final product.

# ********************** Algorithm   ********************** #
def karatsuba(x, y):
    # Base case: if either x or y is less than 10, multiply and return
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)),len(str(y))) # The size of the largest number (in terms of digits)
        mid = int(n/2) # Half of the digits of the largest number
        power = 10**mid # 10**n/2
        a = x // power # First half of the first number
        b = x % power # Second half of the first number
        c = y // power # First half of the second number
        d = y % power # Second half of the second number
        
        # Recursively compute ac, bd, and acbd
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        acbd = karatsuba(a+b,c+d)-ac-bd

        # Compute the result using the Karatsuba formula, which is: ac * 10**n + 10**n/2 * acbd + bd
        return ac * (power ** 2) + bd + (acbd * power)
# ********************** Algorithm   ********************** #

print('Hello, this is an exemple of the Karatsuba multiplication algorithm. Please, enter two numbers: ')

x = int(input('First number: '))
y = int(input('Second number: '))

print('The result is:', karatsuba(x, y))