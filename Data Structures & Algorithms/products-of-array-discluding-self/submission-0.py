class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        output = [0] * len(nums)
        prod = 1

        for i in range(len(nums)):
            if i == 0:
                prefix [i] = prod
            else:
                prod = prod * nums[i-1]
                prefix[i] = prod

        prod = 1

        for j in range(len(nums)-1,-1,-1):
            if j == len(nums) - 1:
                suffix[j] = prod
            else:
                prod = prod * nums[j+1]
                suffix[j] = prod
        
        for k in range(len(nums)):
            output[k] = prefix[k] * suffix[k] 

        return output