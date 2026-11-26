class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        b=False
        for i in nums:
            if i in seen:
                b=True
            else:
                seen.add(i)
        return b
        