class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_group = {}
        
        for s in strs:
            
            alphabets = [0] * 26
            
            for char in s:
                alphabets[ord(char) - ord("a")] +=1
            
            key = tuple(alphabets)

            if key in word_group:
                word_group[key].append(s)
            else:
                word_group[key] = [s]

        return list(word_group.values())