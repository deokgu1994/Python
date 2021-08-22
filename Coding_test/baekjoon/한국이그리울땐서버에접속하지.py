import unittest


import re
def solution(s):
    N = int(input())
    re_s = input()
    pre_s = re_s[:re_s.find("*")]
    back_s = re_s[re_s.rfind("*")+1:]
    for _ in range(N):
        string = input()
        if string[:len(pre_s)] == pre_s or pre_s == "":
            string = string[len(pre_s):]
            if string[-len(back_s):] == back_s or back_s == "":
                print("DA")
                continue
        print("NE")


s = """3
a*
abccd
anestonestod
facebook"""
t ="""6
hho*tan
huhovdjestvarnomozedocisvastan
honijezakon
atila
je
hhotan
hun"""

class SimpleTest(unittest.TestCase):
    def testsolution(self):
        self.assertEqual(solution(s), "DA\nDA\nNE")
        # self.assertEqual(solution(t), "DA\nDA\nNE")

    pass

if __name__ == "__main__":
    # unittest.main()
    solution(s)



