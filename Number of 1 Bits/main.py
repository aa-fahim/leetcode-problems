```
  Solution 1: Convert to string and count number of 1 bits
    
  Time Complexity: O(n) where n is the number of bits in the binary number
```

class Solution:
    def hammingWeight(self, n: int) -> int:

        sum = 0
        strBinaryInt = format(n, "0b")
        for i in strBinaryInt:
            if i == '1':
                sum += 1
        
        return sum
      
```
  Solution 2: The bit operation n & (n-1) removes the rightmost 1 bit. Keep doing this until there are no more 1 bits. Count the number of operations.
    
  Time Complexity: O(m) where m is the number of 1 bits in the binary number.
```

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        sum = 0
        while(int(n) != 0):
            n &= (n-1)
            sum += 1
        
        return sum
