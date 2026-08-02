class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        removed=0

        while l<r:

            if (s[l]) == (s[r]):
                l+=1
                r-=1
            
            else:
                skip_right=s[l:r]
                skip_left= s[l+1:r+1]

                return (skip_left == skip_left[::-1]) or (skip_right==skip_right[::-1])

        return True