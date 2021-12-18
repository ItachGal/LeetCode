class Solution:
    def getMinDistanceToANegativeValue(self, nums: List[int], currStart: int, currEnd: int) -> int:
        length = currEnd-1 - currStart + 1
        for pos in range(0, length):
            if nums[currStart+pos]<0 or  nums[currEnd-1-pos]<0:
                return pos+1
    
    def getMaxLenOfSubArray(self, nums: List[int], currNeg: int, currStart: int, currEnd: int, currMax: int) -> int:
        toRem = 0
        if currNeg%2 == 1:
            toRem = self.getMinDistanceToANegativeValue(nums, currStart, currEnd)                        
        length = currEnd-1 - currStart + 1 - toRem
        return max(length, currMax)
    
    def getMaxLen(self, nums: List[int]) -> int:
        lastPos, currMax, currStart, currEnd, currNeg = 0, 0, 0, 0, 0, 
        listLength = len(nums)
        while(lastPos<listLength):
            if nums[lastPos] == 0:
                currMax = self.getMaxLenOfSubArray(nums, currNeg, currStart, currEnd, currMax)
                lastPos, currStart, currEnd = lastPos+1, lastPos, lastPos
                currStart = currEnd = lastPos
                currNeg = 0
                continue
            if nums[lastPos]<0:
                currNeg = currNeg + 1
            currEnd = currEnd + 1
            lastPos = lastPos + 1
        currMax = self.getMaxLenOfSubArray(nums, currNeg, currStart, currEnd, currMax)
        return currMax
        
