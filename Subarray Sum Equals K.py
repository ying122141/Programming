class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum = count = 0 
        cum_hashmap = {0:1}
        
        for n in nums:
            cum += n
            if cum - k in cum_hashmap:
                count += cum_hashmap[cum - k]
            
            if cum in cum_hashmap:
                cum_hashmap[cum] += 1
            else:
                cum_hashmap[cum] = 1
                
        return count
            
            