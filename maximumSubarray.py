from typing import List
def maxSubArray( nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        currentSum = nums[0]
        for num in nums[1:len(nums)]:
            if currentSum < 0:
                currentSum = num
            else:
                 currentSum += num
        return currentSum


def main():
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

main()