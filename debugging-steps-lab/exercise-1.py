"""
Exercise 1

PART 1: Gather Information
Gather information about the source of the error and paste your findings here. E.g.:
- What is the expected vs. the actual output?
- What error message (if any) is there?
- What line number is causing the error?
- What can you deduce about the cause of the error?

PART 2: State Assumptions
State your assumptions here or say them out loud to your partner ...
Make sure to be SPECIFIC about what each of your assumptions is!

Answer:
IndexError: list index out of range
line 23, in find_largest_diff
 diff = abs(list_of_nums[i] - list_of_nums[i+1])

The developer set the range to len(list_of_nums) which throws an error for diff because range starts from 0 and stops at the index 1 before the length of list_of_nums, making the last i+1 out of range.

This can be fixed by setting the range to len(list_of_nums)-1
"""


def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)-1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)
