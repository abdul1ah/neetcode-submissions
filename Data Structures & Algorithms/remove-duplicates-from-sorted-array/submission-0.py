class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0

        while j < len(nums):
            j= i+1

            if j < len(nums) and nums[i] == nums[j]:
                
                while j < len(nums) and nums[i] == nums[j]:
            
                    nums.remove(nums[j])
    
            i += 1
        return len(nums)
