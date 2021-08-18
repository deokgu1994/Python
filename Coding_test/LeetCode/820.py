import sys 
import time
def minimumLengthEncoding(words):
    # good = set(words)
    # print(f"good {good}")
    # for word in words:
    #     for k in range(1, len(word)):
    #         print(word[k:])
    #         good.discard(word[k:])
    #         print(good)
    # return sum(len(word) + 1 for word in good)        

    # sys.exit()

    words.sort(reverse=True)
    s = words[0]
    words = words[1:]
    if len(words) == 0:
        return len(s)+1

    w_index = 0
    s_index = 0
    is_matching = False
    while w_index < len(words):
        word = words[w_index]
        for _str in word:
            if s[s_index] != _str:
                if is_matching:
                    is_matching = False
                    break
            else:
                is_matching = True
            if s_index >= len(s) -1:
                if not is_matching:
                    print("!!!")
                    s += f"#{word}"
                else:
                    print("@@@")
                    if s_index -1 != len(word):
                        s += f"#{word[s_index:]}"
                w_index +=1
                is_matching = False
                s_index = 0
                break
            s_index +=1        
        time.sleep(0.2)
        print(s)
    return len(s) + 1

    # _index = 0
    # s_i = 0
    # while _index > len(words):
    #     word = word[_index]
    #     if s_i >= len(s):
    #         s += word
        
    pass

if __name__ == "__main__":
    print(minimumLengthEncoding(["time", "me", "bell", "t"])) # 10
    # print(minimumLengthEncoding(["time", "ma", "bell"])) # 13
    # print(minimumLengthEncoding(["time"])) # 5
    # print(minimumLengthEncoding(["me", "time"])) # 5
    # print(minimumLengthEncoding(["ctxdic","c"])) # 5