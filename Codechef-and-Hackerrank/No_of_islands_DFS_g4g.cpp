/*
Question Link: https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1

Given a Matrix consisting of 0s and 1s. 
Find the number of islands of connected 1s present in the matrix. 
Note: A 1 is said to be connected if it has another 1 around it 
(either of the 8 directions).
*/

/*
The approach is to use DFS, traversing through the list, marking all the adjacent 1's
so that an entire bunch is marked at once and is not counted more than once.
*/

#include <bits/stdc++.h>
using namespace std;

// Declaring the functions
// Parameters: A:Grid, x, y : current x and y coordinates, r, c: dimensions of the grid
void marking(vector<int> A[], int x, int y, int r, int c);
int findIslands(vector<int> A[], int N, int M);

// Driver Code Begins
int main() {
	// No of test cases
    int T;
    cin >> T;
    while (T--) {
		//Dimensions of the grid
        int N, M;
        cin >> N >> M;
		
		// Input the grid
        vector<int> A[N];
        for (int i = 0; i < N; i++) {
            vector<int> temp(M);
            A[i] = temp;
            for (int j = 0; j < M; j++) {
                cin >> A[i][j];
            }
        }
		
		// Calling the function to calculate number of islands
        cout << findIslands(A, N, M) << endl;
    }
    return 0;
}
// Driver Code Ends

// Function to traverse in all 8 directions from a point in the grid
void marking(vector<int> A[], int x, int y, int r, int c) {
    
	// If the coordinates are out of bound or the point is either visited, or water, just return
    if(x < 0 || x >= r || y < 0 || y >= c || A[x][y] != 1)
        return;
    
	// Mark the point as visited
    A[x][y] = 2;
    
	// Traversing in all the 8 directions and marking respectively
	// This is done so that the entire island (all points on it) gets marked
    marking(A, x - 1, y - 1, r, c);
    marking(A, x - 1, y, r, c);
    marking(A, x - 1, y + 1, r, c);
    marking(A, x, y - 1, r, c);
    marking(A, x, y + 1, r, c);
    marking(A, x + 1, y - 1, r, c);
    marking(A, x + 1, y, r, c);
    marking(A, x + 1, y + 1, r, c);
}

// Function to calculate no of islands
int findIslands(vector<int> A[], int N, int M) {

    // Initializing paramenters, num = number of islands in the grid
    int i, j, num = 0;
    
	// Traversing through every point in grid
    for(i=0;i<N;i++)
    {
        for(j=0;j<M;j++)
        {
			// If the point is land and is not visited
            if(A[i][j] == 1)
            {
				// Mark the entire island as visited
                marking(A, i, j, N, M);
				// Increment number of islands by one
                num += 1;
            }
        }
    }
    
	// Return number of islands visited
    return num;   
}