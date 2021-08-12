"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


 Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

"""
def solution(_list):
    _list = _list[::-1]
    f_list = _list[0]
    for i in range(1,len(_list)):
        for x, y in enumerate(_list[i]):
            f_list[x] = min(f_list[x],f_list[x+1]) + y
    
    return f_list[0]

if __name__ == "__main__":
    print(solution([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
    print(solution([[-10]]))