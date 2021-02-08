from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        initial = "0000"
        visited = set(deadends)
        if initial in visited:
            return -1
        visited.add(initial)
        queue = [(0,initial)]
        total_steps = -1
        while len(queue) > 0:
            steps, combination = queue.pop(0)
            print(combination)
            if combination == target:
                total_steps = steps
                break
            for index, digit in enumerate(combination):
                new_digit_1 = None
                new_digit_2 = None
                if digit == '9':
                    new_digit_1 = '0'
                    new_digit_2 = '8'
                elif digit == '0':
                    new_digit_1 = '1'
                    new_digit_2 = '9'
                else:
                    new_digit_1 = chr(ord(digit) - 1)
                    new_digit_2 = chr(ord(digit) + 1)
                new_combination_1 = combination[:index] + new_digit_1 + combination[index+1:]
                new_combination_2 = combination[:index] + new_digit_2 + combination[index+1:]
                if not new_combination_1 in visited:
                    visited.add(new_combination_1)
                    queue.append((steps+1, new_combination_1))
                if not new_combination_2 in visited:
                    visited.add(new_combination_2)
                    queue.append((steps+1, new_combination_2))
        return total_steps