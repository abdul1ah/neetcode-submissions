class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        target_freq_count = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            target_freq_count[ord(s1[i]) - ord("a")] += 1
            window[ord(s2[i]) - ord("a")] += 1

        if target_freq_count == window:
            return True

        l = 0 
        r = len(s1)

        while r < len(s2):
            window[ord(s2[r]) - ord("a")] += 1
            window[ord(s2[l]) - ord("a")] -= 1

            if target_freq_count == window:
                return True
            l += 1
            r += 1
        
        return False