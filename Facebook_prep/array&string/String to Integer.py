class Solution:
    def myAtoi(self, s: str) -> int:
        digits=list()
        res=0
        sign=0
        flag=True
        num=0
        for i in s:
            if i==' ':
                if num>0:
                    break
                if not flag:
                    break
                continue
                
            elif i=='-' or i=='+':
                if num>0:
                    break
                if not flag:
                    break
                if i=='-':
                    sign=1
                else:
                    sign=0
                flag=False
            elif ord('0') <= ord(i) <= ord('9'):
                digits.append(ord(i)-ord('0'))
                num+=1
            else:
                if num>0:
                    break
                else:
                    return 0
        
        digits.reverse()
        
        for i in range(len(digits)):
            res+=digits[i]*(10**i)
        if sign:
            res*=(-1)
        if res>2147483647:
            res = 2147483647
        elif res<-2147483648:
            res = -2147483648
        return res
        