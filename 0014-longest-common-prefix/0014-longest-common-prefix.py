class Solution(object):
    def longestCommonPrefix(self, S):
        if "" in S or S == []:
            return ""
        preix = S[0]
        for i in range(1,len(S)):
            while(preix != ""):
                try:
                    if str.index(str(S[i]),preix) == 0:
                        break
                    else:
                        preix = preix[:-1]
                except:
                
                    preix = preix[:-1]
        return preix