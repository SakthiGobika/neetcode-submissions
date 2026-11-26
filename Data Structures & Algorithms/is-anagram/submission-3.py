class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency={}
        ##frequencyoft={}
        for i in s:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        for i in t:
            if i in frequency:
                frequency[i]-=1
            else:
                frequency[i]=1
        b=True
        for i in frequency.values():
            if i!=0:
                b=False
        return b
        