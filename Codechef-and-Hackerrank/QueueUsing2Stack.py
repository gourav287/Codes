"""
Question link:
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():

    q = int(input())

    old, new = [], []

    for _ in range(q):

        val = list(map(int, input().split()))

        if val[0] == 1:

            if not new:

                first = val[1]

            new.append(val[1])

        elif val[0] == 2:

            if not old:

                while new:

                    old.append(new.pop())
                
            old.pop()
        
        else:

            print(old[-1] if old else first)

if __name__ == "__main__":

    main()
