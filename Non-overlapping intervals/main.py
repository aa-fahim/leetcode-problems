'''
  Greedy Approach Solution
  
  Time Complexity: O(n) where n is the number of intervals in the array
  
  Steps
  1. Sort intervals by starting index
  2. Loop through intervals by starting at index 1
  3. Compare current interval to previous interval
  4. Remove the interval that has the larger endtime as it is bound to make more overlapping intervals with the remaining intervals
    
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        moves = 0
        start = 1
        
        while(start < len(intervals)):
            
            curr = intervals[start]
            prev = intervals[start-1]
            if(self.isOverlapping(curr, prev)):
                if (curr[1] >= prev[1]):
                    del intervals[start]
                    moves += 1
                elif (curr[1] < prev[1]):
                    del intervals[start -1]
                    moves += 1
                
            else:
                start += 1
                
        return moves
            
    def isOverlapping(self, a, b):
        return a[0] < b[1] and b[0] < a[1]
            
