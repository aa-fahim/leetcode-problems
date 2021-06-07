'''
    Using hash table approach
    
    Time Complexity: O(n)
    
    Create hash tables for both strings to count the occurence of each character. Compare if the hash tables are equal.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_table = {}
        t_hash_table = {}
        
        for i in s:
            if i in s_hash_table:
                s_hash_table[i] += 1
            else:
                s_hash_table[i] = 1
        
        for i in t:
            if i in t_hash_table:
                t_hash_table[i] += 1
            else:
                t_hash_table[i] = 1
        
        
        is_equal = True
        
        if (len(t_hash_table) != len(s_hash_table)):
            is_equal = False
            return is_equal
        
        for i in s_hash_table:
            if i in t_hash_table and s_hash_table[i] == t_hash_table[i]:
                continue
            else:
                is_equal = False
                break
                
        print(s_hash_table, t_hash_table)
        return is_equal
