class Solution:
    def romanToInt(self, s: str) -> int:
        
        h = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        preValue = 1000
        
        out = 0
        
        for i in range(len(s)):
            
            currValue = h[s[i]]
            
            if currValue > preValue:
                out += (currValue - preValue * 2)
            else:
                out += currValue
            
            preValue = currValue
            
        
        return out