# Calc bit score of every 3 digit no by given conditions
# bit_score = maxof3*11+minof3*7 upto 2 significant digit
# But we only need the tens place digit for our operation
def CalcBitScore(arr):

    new_arr = []
    
    for i in arr:

        s = str(i)

        max_ = int(max(s))

        min_ = int(min(s))

        new_arr.append(((max_*11 + min_ * 7) // 10) % 10)

    return new_arr

# Calc no of pairs
# Calc bit score of entire array then separate them into groups
# as per their index (even/odd) Then work for both groups
# Merge them at last
def NoOfPairs(arr, n):

    # Function to calculate bit score
    bit_score = CalcBitScore(arr)

    # Check if bit_score is properly taken in
    #print(bit_score)

    # Since we need separate odd and even positioned pairs
    odd, even = {}, {}

    j = 0

    # Traversing as a whole
    while j < n:

        i = bit_score[j]

        # Working on odd positioned elements
        odd[i] = odd[i] + 1 if i in odd.keys() else 1

        j += 1

        # Working on even positioned elements
        if j < n:

            i = bit_score[j]

            even[i] = even[i] + 1 if i in even.keys() else 1

            j += 1

    # Checkup odd and even dicts
    #print(odd, even, sep = "\n")

    # Defining a dictionary to store no of pairs
    pairs = {}

    # Inserting odd indexed pairs first
    for key, val in odd.items():

        if val > 1:

            pairs[key] = min(2, val - 1)

    # Check the status of pairs after odd operation
    #print(pairs)

    for key, val in even.items():

        if val > 1:

            if key in pairs.keys():

                pairs[key] += min(2, val - 1)

            else:

                pairs[key] = min(2, val - 1)

    # Checkup status of pairs after even operation
    #print(pairs)

    # No of pairs possible
    nopair = 0

    # Maximum no of pairs can be 2 only
    for i in pairs.keys():

        nopair += min(2, pairs[i])

    # Return no of pairs possible
    return nopair
    

n = int(input())

arr = list(map(int, input().split()))

val = NoOfPairs(arr, n)

print(val, end = "")
