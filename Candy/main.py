'''
  Time Complexity: O(3* n) where n is the number of elements in the ratings array.
  
  Approach
  
  Initialize two arrays with 1s with the same length as ratings array. Iterate the ratings array from left to right starting at the first index and add 1 to the 
  current index of the first array initialized with 1s. if the current element of the ratings array is greater than the previous element. Now iterate from 
  right to left starting at the second last index, and add 1 to the current index of the second array initialized with 1s if the current element is greater than
  the next element. In the third pass, iterate through the two arrays and take the max at each element and add to an integer variable initialized at 0. 
  The result will be this integer variable.
  
  Notes:
  We can improve the time complexity to O(2 * n) because the third pass is unnessary, we can take the max of res1 and res2 array variable when iterating right to
  left.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res1 = [1 for i in range(len(ratings))]
        res2 = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res1[i] = res1[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                res2[i] = res2[i+1] + 1
        
        count = 0
        for i in range(len(res1)):
            tmp = max(res1[i], res2[i])
            count += tmp
            
        return count
                
        
