"""
A non-empty array A consisting of N integers is given.
The array contains an odd number of elements, and each element of the array can be paired with another element
that has the same value, except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.


Write a function:
    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:
N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""


# Not Done - Fails @
#       small random test n=201 - RUNTIME ERROR tested program terminated with exit code 1
#       medium2medium random test n=100,003 - RUNTIME ERROR tested program terminated with exit code 1
#       big1big random test n=999,999, multiple repetitions - RUNTIME ERROR tested program terminated with exit code 1
# Task Score 66% Correctness 80% Performance 50%


def solution(A):
    A = sorted(A)
    oldNum = A[0]
    for index, value in enumerate(A):
        if index != 0:
            if value == oldNum:
                A[index - 1], A[index] = -1, -1
            else:
                oldNum = value
    x = [x for x in A if x > -1]
    if x[0] is None:
        return 0
    else:
        return x[0]


print(solution([2, 2, 4, 4, 4, 5, 5, 3]))
print(solution([2, 2, 3, 3, 4]))
print(solution([1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, ]))
