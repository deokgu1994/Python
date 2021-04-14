/*
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"


*/

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(const string &a, const string &b)
{
    if (b + a < a + b)
        return true;
    return false;
}

string solution(vector<int> numbers) {
    string answer = "";

    vector<string> strings;

    for (int i : numbers)
        strings.push_back(to_string(i));

    sort(strings.begin(), strings.end(), compare);

    for (auto iter = strings.begin(); iter < strings.end(); ++iter)
        answer += *iter;

    if (answer[0] == '0')
        answer = "0";

    return answer;
}




// python
/*

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

*/

/*
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
*/

