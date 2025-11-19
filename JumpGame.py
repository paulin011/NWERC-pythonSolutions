from typing import List,Deque
import sys

def jump(nums: List[int]) -> int:
    jumpList = [sys.maxsize for i in range(len(nums))]
    jumpList[0] = 0
    for i in range(len(nums)):
        currentJumps = jumpList[i]
        for j in range(1,nums[i]+1):
            if i+j < len(nums):
                jumpList[i+j] = min(jumpList[i+j],currentJumps+1)
    return jumpList[len(nums)-1]

def jump_bfs(nums: List[int]) -> int:
    if len(nums) <= 1:
        return 0
    
    # Queue stores (position, jumps_taken)
    queue = deque([(0, 0)])  # Start at position 0 with 0 jumps
    visited = set([0])       # Track visited positions to avoid cycles
    
    while queue:
        pos, jumps = queue.popleft()
        
        # Try all possible jumps from current position
        for jump_size in range(1, nums[pos] + 1):
            next_pos = pos + jump_size
            
            # If we reach the end, return jumps + 1
            if next_pos >= len(nums) - 1:
                return jumps + 1
            
            # If position not visited, add to queue
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, jumps + 1))
    
    return -1  # If no path found

def jump_greedy(nums: List[int]) -> int:
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps

def main():
      nums = [2,3,1,1,4]
      print(jump(nums))
main()

