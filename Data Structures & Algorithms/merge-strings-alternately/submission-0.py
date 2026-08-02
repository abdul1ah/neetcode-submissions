class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        l_w=0
        r_w=0
        merged=[]

        while l_w < len(word1) or r_w < len(word2):
            if l_w < len(word1):
                merged.append(word1[l_w])
                l_w+=1

            if r_w < len(word2):    
                merged.append(word2[r_w])
                r_w +=1

        return "".join(merged)