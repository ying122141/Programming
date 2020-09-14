class Solution:
    def reverse(self, x: int) -> int:
        
        s = 1
        
        if x < 0:
            x = abs(x)
            s = -1
            
        out = x % 10

        if x < 10:
            return x

        else:
            x = math.floor(x/10)

            while x >= 10:    
                r = x % 10

                out = out*10 + r

                x = math.floor(x/10)

            out = (out * 10 + x) * s
            
            if out < (2**31 - 1) and out > -1 * 2**31:
                return out
            else:
                return 0
