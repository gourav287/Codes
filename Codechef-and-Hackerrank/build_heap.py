#This fuction heapify the passed portion of heap into a max heap
def heapify(arr, n, index):
	
	#We only heapify till last non-leaf node. Processing rest is a waste.
	if index > n // 2 - 1:
		return arr
		
	#Initializing a temporary variable equal to index
	curr = index
	
	#Initializing variables for the child nodes' index
	c1, c2 = curr * 2 + 1, curr * 2 + 2
	
	#Comparing left child to the node
	if c1 < n and arr[curr] < arr[c1]:
		curr = c1
	
	#Comparing right child to the node
	if c2 < n and arr[curr] < arr[c2]:
		curr = c2
	
	#Checking if needs to swap
	if curr != index:
		arr[curr], arr[index] = arr[index], arr[curr]
		#To heapify the swapped sub-tree
		heapify(arr, n, curr)
	
	return arr

#This function creates a max heap from the given array.
def create_heap(arr, n):
	
	#Only heapify from the last non-leaf node to root.
	#Heapifying other nodes(leaf) is a waste of time.
	leng = n // 2 - 1
	
	for i in range(leng, -1, -1):
		arr = heapify(arr, n, i)
	
	return arr

def print_heap(arr, n):
	
	#Directly print the values of heap in the array form.
	print("The max heap as an array:")
	print(*arr)

if __name__ == '__main__':
	
	#Input the normal array
	arr = list(map(int, input().split()))
	
	#Calculate length of the array
	n = len(arr)
	
	#Create the heap with create_heap() function
	arr = create_heap(arr, n)
	
	#Output the created heap
	print_heap(arr, n)