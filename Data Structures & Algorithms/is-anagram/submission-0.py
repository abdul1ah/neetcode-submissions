class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters_s={}
        letters_t={}

        for i in range(len(s)):
            if s[i] not in letters_s:
                letters_s[s[i]]=1
            else:
                letters_s[s[i]] = letters_s[s[i]] + 1
        
        for j in range(len(t)):
            if t[j] not in letters_t:
                letters_t[t[j]]=1
            else:
                letters_t[t[j]] = letters_t[t[j]] + 1
        
        return letters_s == letters_t