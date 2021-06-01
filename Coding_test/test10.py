def convert(num, base):
    T = "0123456789ABCDEF"
    quotient, remainder = divmod(num, base)

    if quotient == 0:
        return T[remainder]
    else:
        return convert(quotient, base) + T[remainder]

def solution(n, t, m, p):
    str_all = ""
    num = 0
    while (len(str_all)) < t*m :
        str_all += str(convert(num, n))
        num += 1 

    answer = str_all[p-1::m]
    return answer



if __name__ == "__main__":
    print(solution(2,4,2,1)) # "0111"
    print(solution(16,16,2,1)) # ""02468ACE11111111""
