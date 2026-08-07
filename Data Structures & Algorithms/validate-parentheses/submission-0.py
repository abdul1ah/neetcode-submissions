class Solution:
    def isValid(self, s: str) -> bool:

        top = 0
        stack = []

        if s:
            top = -1

        for i in range(len(s)):

            if s[i] == "[" or  s[i] == "(" or s[i] == "{":
                stack.append(s[i])
                top += 1

            else:
                if stack:
                    if s[i] == ")":
                        if stack[top] != "(":
                            return False
                        else:
                            stack.pop()
                            top -= 1 
                    
                    elif s[i] == "}":
                        if stack[top] != "{":
                            return False
                        else:
                            stack.pop()
                            top -= 1 

                    elif s[i] == "]":
                        if stack[top] != "[":
                            return False
                        else:
                            stack.pop()
                            top -= 1
                else:
                    return False

        return not stack