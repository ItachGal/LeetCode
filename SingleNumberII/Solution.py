class Solution:
    TIMES = 3
    masks = [ 2**j for j in range(0,32) ]
    def getSumOfBitsInPosition(self,i: int, nums: List[int]):
        return sum([1 for x in nums if (x & self.masks[i])])
    
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0,32):
            ans |= (self.getSumOfBitsInPosition(i, nums)%self.TIMES) << i
        if ans >= 2**31:
            return ans-2**32
        return ans
