class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target=sorted(words)
        wrd_len=len(words[0])
        wind_len=wrd_len*len(words)
        results=[]
        
        for i in range(0,len(s)-wrd_len+1):
            current_wnd_wrds=[s[j:j+wrd_len] for j in range(i,i+wind_len,wrd_len)]
            if sorted(current_wnd_wrds)==target:
                results.append(i)

                
        return results
            