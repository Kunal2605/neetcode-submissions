class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        loop1 = 0
        
        for num in nums:
            loop2 = 0
            for num2 in nums:
                
                if loop2 != loop1 and num == num2:
                    return True
                loop2 += 1

            loop1 += 1
        
        return False