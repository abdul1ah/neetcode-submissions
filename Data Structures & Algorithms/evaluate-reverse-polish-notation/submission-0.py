class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums =[]

        for t in tokens:
            if t == "+":
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(n1+n2)

            elif t == "*":
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(n1*n2)

            elif t == "-":
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(n2 - n1)

            elif t == "/":
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(int(n2/n1))
            else:
                nums.append(int(t))
        return nums[0]