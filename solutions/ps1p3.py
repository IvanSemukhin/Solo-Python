# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging.
# We encourage you to work smart.
# If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a break and cleared your head.

import unittest
s = 'maaifvddthkpqrh'  # comment this string before copy-past.


def ls(st):
    answer = ""
    temp = ""
    for ch in st:
        if len(temp) == 0:
            temp += ch
            answer = temp
        elif ch >= temp[-1]:
            temp += ch
            if len(temp) > len(answer):
                answer = temp
        else:
            temp = ch
    return answer


class TestProblem3(unittest.TestCase):
    def test_ls(self):
        self.assertEqual(ls('hpnlvoosughvik'), 'oosu')
        self.assertEqual(ls('syjbywafjpjnhbm'), 'afjp')
        self.assertEqual(ls('tmhzwuhkxqugeleysfsyzvxs'), 'fsyz')
        self.assertEqual(ls('abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(ls('zyxwvutsrqponmlkjihgfedcba'), 'z')


print("Longest substring in alphabetical order is:", ls(s))

# if __name__ == '__main__':
#     unittest.main()

