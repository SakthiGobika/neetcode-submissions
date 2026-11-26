class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cs={}
        ct={}
        for ch in s:
            if ch in cs:
                cs[ch]+=1
            else:
                cs[ch]=1
        for ch in t:
            if ch in ct:
                ct[ch]+=1
            else:
                ct[ch]=1
        return cs==ct
        