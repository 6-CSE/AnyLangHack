from typing import List

def move_zeros(nums: List[int]) -> None:
    zeros = [i for i, num in enumerate(nums) if num == 0]
    nums.extend(nums.pop(index - i) for i, index in enumerate(zeros))
