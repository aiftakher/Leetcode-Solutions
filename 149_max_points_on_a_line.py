import sys
#sys.stdin = open('Hackerrank/sequence_equation/input.txt','r')
sys.stdout = open('Leetcode/output.txt','w')


def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    n = len(points)
    
    max_num = 1
    for i in range(n):
        x1, y1 = points[i]
        cnt = 1
        for j in range(n):
            if(j<=i):
                continue
            x2, y2 = points[j]
            cnt +=1
            for k in range(n):
                if k<=j or k<=i:
                    continue
                x3, y3 = points[k]
                if (y2 - y1)*(x3-x1) == (y3-y1)*(x2-x1):
                    cnt +=1
            max_num = max(max_num,cnt)
            cnt = 1
    print(max_num)

maxPoints([[0,0]])