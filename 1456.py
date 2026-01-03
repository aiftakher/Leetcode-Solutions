import sys
sys.stdin = open('Leetcode/input.txt','r')
sys.stdout = open('Leetcode/output.txt','w')

def maxVowels(s, k):
    s = list(s)
    n = len(s)
    mx = 0
    for i in range(k):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            mx +=1
    
    cur_best = mx
    for i in range(k,n):
        if s[i-k] == 'a' or s[i-k] == 'e' or s[i-k] == 'i' or s[i-k] == 'o' or s[i-k] == 'u':
            cur_best -=1
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            cur_best +=1
        mx = max(mx, cur_best)
    return print(mx)

maxVowels("leetcode",2)
            


                    
                
                