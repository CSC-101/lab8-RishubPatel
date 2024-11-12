from typing import Optional

def ceiling_div(num1: int, num2: int) -> int: #divides num1 but num2 then rounds up to the nearest 1
    return -(-num1//num2)

def groups_of_3(nums: list[int]) -> list[list[int]]: #groups a list of integers into 3s. If there aren't enough values to fill the last grouping, the last grouping is whatever is still ungrouped.
    return [nums[3 * i: (3 * i) + 3] for i in range(ceiling_div(len(nums), 3))] #Python seems to automatically implement the below version
    #return [nums[i:] if i + 2 >= len(nums) else nums[3 * i: (3 * i) + 3] for i in range(ceiling_div(len(nums), 3))]