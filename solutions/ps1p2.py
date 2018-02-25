# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Number of times bob occurs is: 2

import unittest
s = 'oboboobobobobobyboob'  # comment this string before copy-past.


def occur(st):
    pattern = 'bob'
    count = 0
    while st.find(pattern) >= 0:
        st = st[st.find(pattern) + len(pattern)-1:]
        count += 1
    return count


class TestProblem2(unittest.TestCase):
    def test_occur(self):
        self.assertEqual(occur('nvpuswvvgtxi'), 0)
        self.assertEqual(occur('bobobeewbobbbobkpbobyobobovo'), 6)
        self.assertEqual(occur('bobobofbobbdbobboumoboolmbobbpxu'), 5)
        self.assertEqual(occur('bgfrbobobobobobbbobbobobgbobbobbobobbobbbobbobob'), 16)


print('Number of times bob occurs is', occur(s))

# if __name__ == '__main__':
#     unittest.main()

