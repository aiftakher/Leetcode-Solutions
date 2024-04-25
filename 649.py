import sys
sys.stdin = open('Leetcode/input.txt','r')
sys.stdout = open('Leetcode/output.txt','w')

def predictPartyVictory(senate):
    """
    :type senate: str
    :rtype: str
    """
    senate = list(senate)
    num_R = 0
    num_D = 0
    pos_R = []
    pos_D = []
    for i in range(len(senate)):
        if(senate[i]=='R'):
            num_R +=1
            pos_R.append(i)
        else:
            num_D +=1
            pos_D.append(i)
    if num_R == 0:
        return print('Dire')
    elif num_D == 0:
        return print('Radiant')
    else:
        cur_R = pos_R[0]
        cur_D = pos_D[0]
        idx_R = 0
        idx_D = 0
        found = False
        i = 0
        n = len(senate)
        while (1):
            i = i%n
#        for i in range(len(senate)):
            if(senate[i]=='X'):
                i +=1
                continue
            elif(senate[i]=='R'):
                num_D -=1
                if num_D == 0:
                    return print('Radiant')
                else:
                    j = i + 1
                    while (1):
                        j = j%n
                        if senate[j] == 'D':
                            senate[j] = 'X'
                            break
                        j = j + 1
#                    senate[cur_D] = 'X'
                    idx_D +=1
                    cur_D = pos_D[idx_D]
            elif(senate[i]=='D'):
                num_R -=1
                if num_R == 0:
                    return print('Dire')
                else:
                    j = i + 1
                    while(1):
                        j = j%n
                        if senate[j] == 'R':
                            senate[j] = 'X'
                            break
                        j = j + 1
#                    senate[cur_R] = 'X'
                    idx_R +=1
                    cur_R = pos_R[idx_R]
            
            i = i + 1
#            if (i == len(senate) -1) and (found == False):
#                i = 0
                        

predictPartyVictory('RDD')    