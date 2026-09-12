class Solution(object):
    def isThree(self, n):
        l=[1,n]
        for i in range(2,n//2+1):
            if n%i==0:
                l+=[i]
        if len(l) == 3:
            return True
        return False
        