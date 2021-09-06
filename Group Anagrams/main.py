'''
  Time Complexity: O(n * m) where n is the number of elements in the array and m is the character length of the longest string in the array
  
  Approach sorts each string and checks if the sorted string exists in a hash table. The hash table stores sorted strings along with the index of where anagrams
  of the sorted string belong in the groups array. This index tells us where the already found anagrams of the sorted string are in the groups array.
  
'''
class Solution:  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        hashMap = {}
        
        for str in strs:
            sortedWord = ''.join(sorted(str))
            if sortedWord in hashMap:
                index = hashMap[sortedWord]
                group = groups[index]
                group.append(str)
            else:
                groupsLen = len(groups)
                hashMap[sortedWord] = groupsLen
                groups.append([str])
        
        return groups
                
        
