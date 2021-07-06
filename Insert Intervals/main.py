'''
    Time Complexity: O(n) where n is the number of elements in the interval
    
    Steps
    1. If intervals is empty, insert newInterval and return early
    2. Sort interval
    3. Loop through interval and see if newInterval can be merged with current interval
        - condition: if currentIntervalStart < newIntervalEnd and currentIntervalEnd > newIntervalStart
    4. Flag all indicecs that can be merged with newInterval
        - append index to some temp variable
    5. See if newInterval can be inserted
        - condition: if currentIntervalEnd < newIntervalStart and nextIntervalStart > newIntervalEnd
    6. If there are any intervals flagged to be merged then merge them and return new array
        - take start of first interval and end of last interval

    Notes:
      Room for improvement especially checking if the length of the intervals variable is 1. With the addition of lines 42-44, im not sure if the check is still necessary.
      These lines were implemented after the check.
'''

class Solution:
    def merge_overlapping_intervals(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []: 
            return [newInterval]
        
        if len(intervals) == 1:
            if (intervals[0][0] <= newInterval[1] and intervals[0][1] >= newInterval[0]):
                return [self.merge_overlapping_intervals(newInterval, intervals[0])]
            elif (intervals[0][1] < newInterval[0]):
                return [intervals[0], newInterval]
            else:
                return [newInterval, intervals[0]]
        
        intervals.sort(key=lambda x: x[0])
        
        flaggedIndices = []
        for i in range(len(intervals)):
            currentInterval = intervals[i]
            
            if (i == 0):
                if (currentInterval[0] > newInterval[1]):
                    return [newInterval] + intervals[0:]

            if (currentInterval[0] <= newInterval[1] and currentInterval[1] >= newInterval[0]):
                flaggedIndices.append(i)
            else:
                try:
                    nextInterval = intervals[i + 1]
                    if (currentInterval[1] < newInterval[0] and nextInterval[0] > newInterval[1]):
                        intervals = intervals[:i+1] + [newInterval] + intervals[i+1:]
                except:
                    if (len(flaggedIndices) == 0):
                        intervals.append(newInterval)
       
        if (len(flaggedIndices) > 0):
            startIndex = flaggedIndices[0]
            endIndex = flaggedIndices[-1]
            if (startIndex != endIndex):
                mergedInterval = [min(intervals[startIndex][0], newInterval[0]), max(intervals[endIndex][1], newInterval[1])]
                intervals = intervals[:startIndex] + [mergedInterval] + intervals[endIndex+1:]
            else:
                mergedInterval = self.merge_overlapping_intervals(intervals[startIndex], newInterval)
                intervals[startIndex] = mergedInterval


        
        return intervals
            
        

        
        
