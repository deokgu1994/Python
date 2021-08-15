import sys 

def findAnagrams(s, p):
    answer = []
    for _index, _str in enumerate(s):
        print(f"남은 s {s[_index:]} {_str}")
        if _str in p:
            print(f"찾은")
            temp_index = _index
            temp_p = p[:] 
            for x in range(len(p)):
                if len(s) == temp_index:
                    break
                if s[temp_index] not in temp_p:
                    is_answer = False
                    break
                print(temp_p)
                print("!!!!!!!!!")
                temp_p = temp_p[:p.find(s[temp_index])] + temp_p[p.find(s[temp_index])+1:]
                temp_index += 1
                is_answer =True
            if is_answer:
                answer.append(_index)

    return answer
    pass 


if __name__ == "__main__":
    # print(findAnagrams("cbaebabacd", "abc")) # [0, 6]
    # print(findAnagrams("abab", "ab")) # [0, 1, 2]
    # print(findAnagrams("baa", "aa")) # [1]
    print(findAnagrams("abacbabc", "abc")) # [1,2,3,5]


"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[s[i]] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
"""