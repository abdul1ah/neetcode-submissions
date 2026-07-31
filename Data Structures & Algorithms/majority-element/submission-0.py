class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq_count={}
        
        for i in range (len(nums)):

            if nums[i] in freq_count:
                freq_count[nums[i]] += 1
        
            else:
                freq_count[nums[i]] = 1

        for x in freq_count:
            if freq_count[x] > len(nums)/2:
                return x