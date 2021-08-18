import time
def champagneTower(poured: int, query_row: int, query_glass: int):
    index = 1
    if poured ==1:
        return 0
    while True:
        print(index, poured)
        if 2**index <= poured < 2**(index+1):
            if poured < index:
                return 1
            return ((poured - 2**index) +1)/ 2**index
            break
        else:
            index +=1 
        time.sleep(0.1)
if __name__ == "__main__":
    print(champagneTower(7, 7, 1)) 
    # print(champagneTower(100000009, 33, 17)) # 10