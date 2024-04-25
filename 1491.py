import sys
sys.stdin = open('Leetcode/input.txt','r')
sys.stdout = open('Leetcode/output.txt','w')


class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n = len(salary)
        salary.sort()
        mn = salary[0]
        mx = salary[-1]
        tot = 0.0
        cnt = 0.0
        for i in range(n):
            if salary[i] == mn or salary[i] == mx:
                continue
            tot += salary[i]
            cnt += 1.0
        
        if cnt == 0:
            return 0
        else:
            return float (tot/cnt) 
