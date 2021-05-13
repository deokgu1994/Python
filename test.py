
def solution(board, moves):
    answer = 0
    N = len(board[0])
    _list = [ [] for x in range(N +1)]
    x_borad = board[::-1]
    for board in x_borad:
        for index, num in enumerate(board):
            if num != 0:
                _list[index].append(num)
                
    for x in moves:
        if len(_list[x-1]) > 0:
            compare_num = _list[x-1].pop()
            if len(_list[N]) > 0 and _list[N][-1] == compare_num :
                _list[N].pop()
                answer += 2
            else:
                _list[N].append(compare_num)
    return answer

if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))