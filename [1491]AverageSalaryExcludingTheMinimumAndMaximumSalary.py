from typing import List

def average(salary: List[int]) -> float:
    salary.remove(max(salary))
    salary.remove(min(salary))
    return sum(salary) / len(salary)

print(average([3000, 1000, 2000]))