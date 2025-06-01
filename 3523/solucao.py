class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                num = max(num, stack.pop())
            stack.append(num)
        return len(stack)