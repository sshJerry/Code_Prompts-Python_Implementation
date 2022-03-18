"""
This is a demo task.
Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than O) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [-1, -3), the function should return 1.

Write an efficient algorithm for the following assumptions:
    • N is an integer within the range [1.100,000);
    • each element of array A is an integer within the range [-1,000,000..1,000,000].
"""


def solution(A):
    currentNum = 1
    for nums in sorted(A):
        if currentNum == nums:
            currentNum += 1
    return currentNum

#Test Case 1
print(solution([1, 3, 6, 4, 1, 2, 7, 9, 12, 20]))
#Test Case 2
print(solution([1, 3, 6, 4, 1, 2]))
#Test Case 3
print(solution([1, 2, 3]))
#Test Case 4
print(solution([-1, -3]))