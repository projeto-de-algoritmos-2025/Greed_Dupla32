class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                # Soma da área do possível carimbo (usando soma prefixada)
                total = prefix[i+stampHeight][j+stampWidth] - prefix[i+stampHeight][j] - prefix[i][j+stampWidth] + prefix[i][j]
                if total == 0:
                    diff[i][j] += 1
                    diff[i + stampHeight][j] -= 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1

        cover = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = cover[i-1][j] if i > 0 else 0
                left = cover[i][j-1] if j > 0 else 0
                diag = cover[i-1][j-1] if i > 0 and j > 0 else 0
                cover[i][j] = diff[i][j] + up + left - diag

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cover[i][j] <= 0:
                    return False
        return True
