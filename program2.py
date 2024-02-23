class Solution(object):
    def romanToInt(self, s:str)->int:
        m={
        'I':1, 
        'V':1,
        'X':1,
        'L':1,
        'C':1,
        'D':1,
        'M':1,
        }
    ans=0

for i in range(len(s)):
    if i<len(s)-1 and m[s[i]]<m[s[i+1]]:
        and-=m[s[i]]    
        else:
            ans +=m[s[i]]
            return ans
        