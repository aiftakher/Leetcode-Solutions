# LC_1359.py 

import math

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        sbs = 0
        while 2*n - sbs >= 2:
            # compute permutation(2*n - sbs, 2) / 2


            ans = ans * (math.perm(2*n - sbs, 2) // 2) % MOD
            sbs += 2
        return ans


sol = Solution()
print(sol.countOrders(3)) # 1
