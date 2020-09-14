class Solution:
    def mySqrt(self, x: int) -> int:
        
        maxNum = x
        minNum = 1
        
        midNum = 0
            
        while minNum <= maxNum:
            
            midNum = int((maxNum + minNum) / 2)
            
            squtNum = midNum * midNum
            
            if squtNum == x:
                return midNum
            elif squtNum > x:
                maxNum = midNum - 1
            else:
                minNum = midNum + 1
           
        
        if midNum * midNum > x:
            return int(midNum) - 1
        
        return int(midNum)