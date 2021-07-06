'''
  Approach: Sort Intervals and Loop through Intervals
  
  Time Complexity: O(n) where n is the number of elements in the intervals array
'''
class Solution:
    def merge_overlapping_intervals(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]
    
    '''
    Exceeded Time Limit so i used built-in sort function
    
    def sortInterval(self, interval):
        return interval.sort(key=lambda x: x[0])

        
        res = [interval[0]]
        
        for i in range(1, len(interval)):
            for j in range(len(res)):
                if interval[i][0] < res[j][0]:
                    res.insert(j, interval[i])
                if (j == (len(res) - 1)):
                    res.insert(j+1, interval[i])
                    
        return res
    '''
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(len(intervals)):
            if (intervals[i][0] <= res[-1][1] and intervals[i][1] >= res[-1][0] and i!=0):
                start = res[-1][0]
                end = res[-1][1]
                res.pop()
                res.append(self.merge_overlapping_intervals([start, end], intervals[i]))
            elif i!=0:
                res.append(intervals[i])
            
        return res
