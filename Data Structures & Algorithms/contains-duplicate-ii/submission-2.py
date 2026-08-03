class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} 
        
        for i in range(len(nums)):
            current_num = nums[i]

            if current_num in seen:

                last_seen_index = seen[current_num]
                if abs(i - last_seen_index) <= k:
                    return True
            
            seen[current_num] = i
            
        return False