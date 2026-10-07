class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(x):
            a=""
            if len(x)==1:
                if x=='1':
                    a='0'
                else:
                    a='1'
                return a
            else:
                for i in x:
                    if i=='1':
                        a+='0'
                    else:
                        a+='1'
                return a
        s=[0 for _ in range(n)]
        s[0]="0"
        for i in range(1,n):
            s[i]=s[i-1]+"1"+(''.join(reversed(invert(s[i-1]))))
        return s[n-1][k-1]