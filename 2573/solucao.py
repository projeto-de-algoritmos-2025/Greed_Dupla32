class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        n = len(lcp)
        res = [''] * n
        idx = 0  

        for i in range(n):
            if res[i]:
                continue
            if idx >= 26:
                return ""  
            c = chr(ord('a') + idx)
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = c
            idx += 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    expected = 1
                    if i + 1 < n and j + 1 < n:
                        expected += lcp[i + 1][j + 1]
                    if lcp[i][j] != expected:
                        return ""
                else:
                    if lcp[i][j] != 0:
                        return ""

        return ''.join(res)
