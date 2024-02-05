"""
The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
"""


# def check_exam(arr1, arr2):
#     summer = 0
#     if arr1[0] == arr2[0]:
#         summer += 4
#     else:
#         summer -= 1
#
#     if arr1[1] == arr2[1]:
#         summer += 4
#     else:
#         summer -= 1
#
#     if arr1[2] == arr2[2]:
#         summer += 4
#     else:
#         summer -= 1
#
#     if arr1[3] == arr2[3]:
#         summer += 4
#     else:
#         summer -= 1
#
#     if summer < 0:
#         return 0
#
#     return summer
#

def check_exam(arr1, arr2):
    score = 0

    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr2[i] == arr1[i]:
            score += 4
        else:
            score -= 1

    return max(0, score)

print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))
