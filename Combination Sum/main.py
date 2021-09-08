class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def findCombination(currTarget, arr):
            if currTarget < 0:
                return
            
            if currTarget == 0:
                arr = sorted(arr)
                if arr not in res:
                    res.append(arr)
                return
            
            for i in candidates:
                tmpTarget = currTarget - i
                tmpArr = arr + [i]
                findCombination(tmpTarget, tmpArr)
        
        findCombination(target, [])
        
        return res
