class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create a list of [value, original_index] pairs
        # This solves the duplicate number issue.
        indexed_nums = []
        for i in range(len(nums)):
            indexed_nums.append([nums[i], i])
            
        # 2. Sort based on the values
        indexed_nums.sort()
        
        left = 0
        right = len(indexed_nums) - 1
        
        # 3. Use two pointers to find the target
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return indices in ascending order
                idx1 = indexed_nums[left][1]
                idx2 = indexed_nums[right][1]
                return [idx1, idx2] if idx1 < idx2 else [idx2, idx1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []