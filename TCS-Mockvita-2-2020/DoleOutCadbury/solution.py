# Taking inputs
p = int(input())
q = int(input())
r = int(input())
s = int(input())

# No of candies initially
noc = 0

# Working for all the lengths
for i in range(p, q+1):

    # Working for all the widths
    for j in range(r, s+1):

        # The working code
        # A child will always get cadbury of size b * b
        # and remaining part will be b*(a%b)
        # After b = 1, it will be divided into a parts
        # of dimensions 1 * 1 each
        a, b = max(i, j), min(i, j)

        while b > 1:

            noc += a // b

            a, b = b, a % b

        noc += a if b == 1 else 0

print(noc, end = "")
