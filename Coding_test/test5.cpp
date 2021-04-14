/*
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
*/

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#define MAX 9999999999
using namespace std;

bool isPrime(int number)
{
    if (number == 1)
        return false;
    if (number == 2)
        return true;
    if (number % 2 == 0)
        return false;

    bool isPrime = true;
    for (int i = 2; i <= sqrt(number); i++)
    {
        if (number% i == 0)
            return false;
    }

    return isPrime;
}

bool compare(char a, char b)
{
    return a > b;
}

int solution(string numbers) {
    int answer = 0;

    string temp;
    temp = numbers;

    sort(temp.begin(), temp.end(),compare);

    vector<bool> prime(std::stoi(temp)+1);

    //cout << stoi(temp) << endl;
    prime[0] = false;
    for (long long i = 1; i < prime.size(); i++)
    {
        prime[i] = isPrime(i);
    }
    //cout << "chk1" << endl;
    //int num = std::stoi(numbers);

    string s, sub;

    s = numbers;

    sort(s.begin(), s.end());
    set<int> primes;
    int l = s.size();
    do {
        for (int i = 1; i <= l; i++)
        {
            sub = s.substr(0, i);
        //  cout << "chk2" <<  " " << sub<<  endl;
            if (prime[std::stoi(sub)])
            {
                primes.insert(std::stoi(sub));
            }
        }
    } while (next_permutation(s.begin(), s.end()));

    //cout << primes.size();
    answer = primes.size();
    return answer;
}

/*

# 0으로 시작하는 숫자. 
# 모든 숫자의 조합.

def isPrimeNumber(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True

def getAllCombination(numbers, numList, leftCipher):
    '''
    numbers : 총 숫자카드 list
    numList : 가능한 숫자 배열 list
    leftCipher : 남은 자릿수
    '''

    # 현재 가능한 숫자 배열 list를 기준으로 추가가 가능한 숫자들은 찾는다. 
    newNumList = [[]]
    for li in numList:
        for i in numbers:
            if i in li and li.count(i) <= numbers.count(i) - 1:
                tmp = li[:]
                tmp.append(i)
                newNumList.append(tmp)
            if i not in li:
                tmp = li[:]
                tmp.append(i)
                newNumList.append(tmp)

    leftCipher -= 1

    if leftCipher == 0:
        return newNumList
    else:
        return getAllCombination(numbers, newNumList, leftCipher)

def removeFirstZero(numList):
    for i, num in enumerate(numList):
        firstNumIsZero = bool()

        while True:
            if len(num) >= 2 and num[0] == '0':
                firstNumIsZero = True
            else:
                numList[i] = num
                break

            num = num[1:]

def getUnique2DList(numList):
    for i, val in enumerate(numList):
        tmp = str()
        for char in val:
            tmp += char
        numList[i] = tmp

    newList = list(set(numList))
    return newList

def solution(numbers):    
    availableAnswer = getAllCombination(numbers, [[]], len(numbers))
    del availableAnswer[0]
    removeFirstZero(availableAnswer)
    availableAnswer = getUnique2DList(availableAnswer)

    answer = 0
    for val in availableAnswer:
        if isPrimeNumber(int(val)):
            print(val)
            answer += 1

    return answer
*/


/*

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

*/