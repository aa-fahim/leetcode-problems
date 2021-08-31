'''
  Time Complexity: O(n) where n is the number of characters in the string
  
  Solution trims the non-ASCII characters from the string first. Then splits the trimmed string into a list, reverses the list, and joins the list back into a single
  string. If the trimmed string and reversed string are equal than the string is a valid palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmedString = ''.join([i.lower() for i in s if i.isalnum()])
        
        tmp = split('', trimmedString)
        tmp.reverse()
        reversedString = ''.join(tmp)

        if trimmedString == reversedString:
            return True

        return False
            
