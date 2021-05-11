import pandas as pd 
import sys

def x_to_arry(y, index):
    print(y)
    y= y.split(' ')
    for _index, text in enumerate(y):
        if "x" in text:
            if text[-1] == "x":
                t = "1"
            else:
                t = text[text.find("x") +1]
            y[_index] = text[:text.find("x")] + "*np.power(index_array_" +  str(index) +"," + t + ")"
    return " ".join(y)
    
    
if __name__ == "__main__":
    df = pd.read_excel("test.xlsx", usecols=[1]).dropna()
    df = df.to_dict()
    b = []
    index = 0
    print()
    for _dict in df.values():
        for text in _dict.values():
            index += 1
            b.append(x_to_arry(text, index))
    
    temp_df = pd.DataFrame(b)

    temp_df.to_excel("sucess.xlsx")
