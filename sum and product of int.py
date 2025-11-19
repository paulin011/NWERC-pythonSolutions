# No additional imports needed for this problem

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 0
        number = str(n)
        product, sum = 1,0
        for c in number:
            product = product * int(c)
            sum += int(c)
        return product - sum
        

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Example from LeetCode (n = 234)
    n1 = 234
    result1 = solution.subtractProductAndSum(n1)
    print(f"Test 1: n = {n1}")
    print(f"Result: {result1}")
    print()
    
    # Test case 2: Example from LeetCode (n = 4421)
    n2 = 4421
    result2 = solution.subtractProductAndSum(n2)
    print(f"Test 2: n = {n2}")
    print(f"Result: {result2}")
    print()
    
    # Test case 3: Single digit
    n3 = 5
    result3 = solution.subtractProductAndSum(n3)
    print(f"Test 3: n = {n3}")
    print(f"Result: {result3}")
    print()
    
    # Test case 4: Number with zero
    n4 = 105
    result4 = solution.subtractProductAndSum(n4)
    print(f"Test 4: n = {n4}")
    print(f"Result: {result4}")
    print()
    
    # Test case 5: Larger number
    n5 = 9876
    result5 = solution.subtractProductAndSum(n5)
    print(f"Test 5: n = {n5}")
    print(f"Result: {result5}")
    print()
    
    # Test case 6: Two digit number
    n6 = 98
    result6 = solution.subtractProductAndSum(n6)
    print(f"Test 6: n = {n6}")
    print(f"Result: {result6}")
    print()