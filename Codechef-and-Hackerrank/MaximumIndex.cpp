/*
Question link:
	https://practice.geeksforgeeks.org/problems/maximum-index3307/1

Given an array Arr[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of Arr[i] <= Arr[j].
*/

// Required format as per the question
class Solution{

public:

    int maxIndexDiff(int arr[], int n) {

        // Create 2 vectors named increasing and decreasing
        vector<int>increasing(n,arr[n-1]),decreasing(n,arr[0]);
        
		// Iterating through the length of array arr
        for(int i=1;i<n;i++)
            
			// Decreasing value array will always have minimum of the yet traversed values
            decreasing[i]=min(arr[i],decreasing[i-1]);
        
		// Reversely iterating through the length of array arr
        for(int i=n-2;i>=0;i--)
            
			// Increasing value array will always have maximum of the yet traversed values
            increasing[i]=max(arr[i],increasing[i+1]);
        
		// Initialize some required variables
        int i = 0, j = 0, answer=0;
        
		// Iterating through the increasing and decreasing vectors
        while(i<n && j<n)
        { 
            
			// Trying to store the greatest value of i - j
            if(increasing[i]>=decreasing[j])
            {
                
                answer=max(answer,i-j);
                
                i++;
            }
			
            else{
                
                j++;
            }
        }
        
		// Returning the answer
        return answer;
    }

};