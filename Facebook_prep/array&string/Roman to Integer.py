class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        map={}
        map['I']=1
        map['V']=5
        map['X']=10
        map['L']=50
        map['C']=100
        map['D']=500
        map['M']=1000
        
        s=reversed(s)
        s = ''.join(s)
        i = 0
        while True:
            if i>len(s)-2:
                break
            if map[s[i]]>map[s[i+1]]:
                value = map[s[i]]-map[s[i+1]]
                res+=value
                i+=2
            else:
                value = map[s[i]]
                res+=value
                i+=1
        if i==len(s)-1:
            res+=map[s[i]]
        
        return res
            
                
                