# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.

# 예를 들어

# d(91) = 9 + 1 + 91 = 101

# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.

# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 그런데 반대로, 제네레이터가 없는 숫자들도 있으며,
#  이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

# def solution1(maxnum):
#     safty_nums = [x for x in range(maxnum+1)]
#     for x in range(maxnum+1):
#         print(x)
#         jenerate_num = ((x%10000)//1000) + ((x%1000)//100) + ((x%100)//10) + (x%10) + x
#         if jenerate_num in safty_nums:
#             safty_nums.remove(jenerate_num)
#     anser = safty_nums
#     return  anser

# sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)})

# def solution2(num):
#     answer = [str(x).count("8") for x in range(num)]
#     return sum(answer)

#     str(list(range(1,num+1))).count('8')    
    

if __name__ == "__main__":
    # print(solution1(5000))
    # print(solution2(10000))