"""
In this task we consider interesting patterns that could be observed on a digital clock. Such clock displays current
time using the format "HH:MM:SS" where:
    "HH" is the hour of the day (00 through 23), as two decimal digits; •
    "MM" is the minute within the hour (00 through 59), as two decimal digits; •
    "SS" is the second within the minute (00 through 59), as two decimal digits
Note that hour, minute and second are always represented as two digits, so the clock displays leading zeros if needed.
We say that a point in time is interesting if digital clock needs at most two distinct digits to display it.
For example, 13:31:33 and 02:20:22 are, both interesting, because digital clock can display it using only
digits 1 and 3 in the first case, or o and 2 in the second one. 00:00:00 is interesting too,
as it can be displayed using only o, but 15:45:14 is not, due to the fact that more than two distinct digits are used.
Note that delimiter character ":" is permanently printed onto clock's display and doesn't count as one
of displayed digits. Your task is to count interesting points in time in a given period of time.


Write a function:
    class Solution { public int solution(String S, String T); }
that, given strings S and T representing time in the format "HH:MM:55", returns the number of interesting points
in time between S and T (inclusive).


For example, given "15:15:00" and "15:15:12", your function should return 1,
because there is only one interesting point in time between these points (namely "15:15:11"),
Given "22:22:21" and "22:22:23", your function should return 3;
interesting points in time are "22:22:21", "22:22:22",, and "22:22:23".


Assume that:
    • strings S and T follow the format "HH:MM:SS" strictly
    • string S describes a point in time before T on the same day.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""


def solution(S, T):
    lis1, lis2, finalList = [
                                str(S[0]) + str(S[1]),
                                str(S[3]) + str(S[4]),
                                str(S[6]) + str(S[7]),
                            ], [
                                str(T[0]) + str(T[1]),
                                str(T[3]) + str(T[4]),
                                str(T[6]) + str(T[7]),
                            ], []
    minutes, seconds, startHour, startMin, startSec, interCount = 60, 60, int(lis1[0]), int(lis1[1]), int(lis1[2]), 0

    for h in range(startHour, int(lis2[0]) + 1):
        if h == int(lis2[0]):
            minutes = int(lis2[1]) + 1
        for m in range(startMin, minutes):
            if h == int(lis2[0]) and m == int(lis2[1]):
                seconds = int(lis2[2]) + 1
            for s in range(startSec, seconds):
                finalList.append([str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)])
        startMin, startSec = 0, 0

    for x in range(len(finalList)):
        finalSet = set()
        for y in range(3):
            finalSet.add(finalList[x][y][0:1])
            finalSet.add(finalList[x][y][1:2])
        if len(finalSet) <= 2:
            interCount += 1
    return interCount


# Test #1
print(solution('01:00:00', '03:11:11'))
# Test #2
print(solution('01:58:55', '02:01:05'))
# Test #3
print(solution('15:15:00', '15:15:12'))
