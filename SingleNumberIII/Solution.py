# https://leetcode.com/problems/single-number-iii/submissions/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        v1 = reduce(operator.xor, nums)
        lsb = v1 & (v1-1) ^ v1
        v2 = reduce(xor, filter(lambda num: num & lsb, nums))
        return [v2, v2^v1]
        
