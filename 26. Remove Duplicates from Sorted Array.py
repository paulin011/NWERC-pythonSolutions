from typing import List

def removeDuplicates(nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique = {nums[0]:1}
        i = 1
        while i < len(nums):
            if unique.get(nums[i],-1) == -1:
                unique[nums[i]] = 1
                i+=1            
            else:
                nums.pop(i)

        return i    
def main():
    Lis = [1,1,2]
    print(removeDuplicates(Lis))
    print(Lis)

main()