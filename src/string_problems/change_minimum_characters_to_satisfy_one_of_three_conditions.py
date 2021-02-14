#!/usr/bin/env python
"""
Platform: LeetCode
1737. Change Minimum Characters to Satisfy One of Three Conditions
URL: https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

Description:
You are given two strings a and b that consist of lowercase letters.
In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.


Example 1:
Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations,
then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

Example 2:
Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".

Constraints:
1 <= a.length, b.length <= 105
a and b consist only of lowercase letters.

Complexity: Time O(A + B), Space O(1)
"""
from collections import Counter


class Solution:
    def min_characters(self, a: str, b: str) -> int:
        ca = Counter(a)  # O(A)
        cb = Counter(b)  # O(B)
        ret = len(a) + len(b) - max((ca + cb).values())  # case 3
        # loop through every letter in the alphabet
        for c in "bcdefghijklmnopqrstuvwxyz":  # O(1)
            # c will be the pivot
            cnt_1 = cnt_2 = 0
            # loop through the frequencies of each letter in a
            for char_ca, cnt_ca in ca.items():  # O(1)
                # in the first case we want to make every letter in a smaller than the pivot
                if char_ca < c:
                    cnt_2 += cnt_ca
                # for the second case we want to make them bigger or equal
                else:
                    cnt_1 += cnt_ca
            # when looping b, swap the conditions
            for char_cb, cnt_cb in cb.items():  # O(1)
                if char_cb < c:
                    cnt_1 += cnt_cb
                else:
                    cnt_2 += cnt_cb
            # check which of the three cases has the smallest cost
            ret = min([ret, cnt_1, cnt_2])
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_characters(a="aba", b="caa") == 2
    assert solution.min_characters(a="dabadd", b="cda") == 3
