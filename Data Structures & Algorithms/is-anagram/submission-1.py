class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyofs={}
        frequencyoft={}
        for i in s:
            frequencyofs[i]=frequencyofs.get(i,0)+1
        for i in t:
            frequencyoft[i]=frequencyoft.get(i,0)+1
        return frequencyofs==frequencyoft
        