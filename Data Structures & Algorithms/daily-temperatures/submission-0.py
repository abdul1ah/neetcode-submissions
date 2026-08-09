class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                cooler_temp, cooler_index = stack.pop()

                days_ahead = i - cooler_index

                result[cooler_index] = days_ahead

            stack.append((t,i))

        return result