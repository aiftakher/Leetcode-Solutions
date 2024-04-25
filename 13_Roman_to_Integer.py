def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        i = 0
        n = len(s)
        while(i<n):
            if i < n-1:
                if s[i] == 'I' and s[i+1] == 'V':
                     val += 4
                     i+=2
                elif s[i] == 'I' and s[i+1] == 'X':
                     val += 9
                     i+=2
                elif s[i] == 'X' and s[i+1] == 'L':
                     val += 40
                     i+=2
                elif s[i] == 'X' and s[i+1] == 'C':
                     val += 90
                     i+=2
                elif s[i] == 'C' and s[i+1] == 'D':
                     val += 400
                     i+=2
                elif s[i] == 'C' and s[i+1] == 'M':
                     val += 900
                     i+=2
                else:                     
                    if s[i] == 'I':
                         val +=1
                         i+=1
                    elif s[i] == 'V':
                         val +=5
                         i+=1
                    elif s[i] == 'X':
                         val +=10
                         i+=1
                    elif s[i] == 'L':
                         val +=50
                         i+=1
                    elif s[i] == 'C':
                         val +=100
                         i+=1       
                    elif s[i] == 'D':
                         val +=500
                         i+=1     
                    elif s[i] == 'M':
                         val +=1000
                         i+=1
            else:
                    if s[i] == 'I':
                         val +=1
                         i+=1
                    elif s[i] == 'V':
                         val +=5
                         i+=1
                    elif s[i] == 'X':
                         val +=10
                         i+=1
                    elif s[i] == 'L':
                         val +=50
                         i+=1
                    elif s[i] == 'C':
                         val +=100
                         i+=1         
                    elif s[i] == 'D':
                         val +=500
                         i+=1     
                    elif s[i] == 'M':
                         val +=1000
                         i+=1     
        
        
        print(val)
romanToInt("MCMXCIV")
        