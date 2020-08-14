# Function to calculate no of pairs remained
# Logic is to check for the required groom index
# Then moving all the preceeding grooms at the end and moving on
# If groom not found, remaining bride will be the number of pairs remained
def swayamvar(b, g):
  
  i = 0
  
  n = len(b)
  
  while i < n:
    
    d = g.find(b[0])
    
    if d < 0:
      
      break
     
    g = g[d+1:] + g[:d]
    
    b = b[1:]
    
    i += 1

    return d

n = int(input())

bride = input()

groom = input()

print(swayamvar(bride, groom))
