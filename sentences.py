from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxL = 0
        for sentence in sentences:
            maxL = max(maxL,sentence.count(" ")+1)
        return maxL

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic example
    sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    result1 = solution.mostWordsFound(sentences1)
    print(f"Test 1: {sentences1}")
    print(f"Result: {result1} Expected 6")
    print()
    
    # Test case 2: Single word sentences
    sentences2 = ["hello", "world", "python"]
    result2 = solution.mostWordsFound(sentences2)
    print(f"Test 2: {sentences2}")
    print(f"Result: {result2}")
    print()
    
    # Test case 3: One sentence with many words
    sentences3 = ["this sentence has many words in it", "short", "ok"]
    result3 = solution.mostWordsFound(sentences3)
    print(f"Test 3: {sentences3}")
    print(f"Result: {result3}")
    print()
    
    # Test case 4: Empty spaces and punctuation
    sentences4 = ["hello world!", "this is a test", "a", "multiple spaces  here"]
    result4 = solution.mostWordsFound(sentences4)
    print(f"Test 4: {sentences4}")
    print(f"Result: {result4}")
    print()
    
    # Test case 5: Single sentence
    sentences5 = ["only one sentence with several words"]
    result5 = solution.mostWordsFound(sentences5)
    print(f"Test 5: {sentences5}")
    print(f"Result: {result5}")
    print()
    
