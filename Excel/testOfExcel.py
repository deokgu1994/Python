import pandas as pd # impor는 사용하는 모듈을 호출할때 사용한다.  import ?? as ??? 의 as는 별칭으로 앞의 ?? 대신에 쉽게 이름을 설정하여 ???을 사용할 수 있다. 

df = pd.read_excel("test.xlsx")# .T (행과 열의 위치를 바꿔서 저장한다.)
#print(df)

df[1::2].to_excel("odd.xlsx")
print(df[1::2].T)
# 밑에 갔다가 오세요~
## 밑에서 다시 올라옴
print(df)
#   Unnamed: 1 Unnamed: 2 Unnamed: 3 Unnamed: 4 Unnamed: 5 ## << colums
# 0        NaN        NaN        NaN        NaN        NaN
# 1      TEST      test_1     test_2     test_3     test_4
# 2          1          2          3          4          5
# ^
# ^ rows
df.drop(["Unnamed: 0", "Unnamed: 2"], axis = 1, inplace = True)
df.to_excel("sucess.xlsx")
##



# import openpyxl # xlxs로 자동화 스크립트를 작성할때는  openpyxl를 많이 사용한다고합니다.

# wb = openpyxl.load_workbook("test.xlsx")
# print(df) # 읽으로 읽으면 <openpyxl.workbook.workbook.Workbook object at 0x0D587AA8> 형식으로 읽히는데 이거는 이것이 객체라는 타입으로 받기 때문이다.
# print(type(df)) #로 읽을시 이 df변수의 타입을 말하고 있습니다.
# # python에서는 여러가지 타입이 있습니다. int, str, list, dict 등등이 있습니다. 
# int_test = 10
# print(type(int_test))
# str_test = "test"
# print(type(str_test))
# list_test = []
# print(type(list_test))
# dict_test = {}
# print(type(dict_test))
# # 이것들을 잘 활용해야합니다. 
# # print(dir(int_test))
# print(dir(str_test)) # 출력되는것을 모두 함수로 사용할수 있는데 이유는 "str"이라는 클래스로 정의 되어있기 때문에 클래스안에 있는 매소드를 호출 합니다.
# print(str_test.split("s"))
# print(str_test.upper()) # 이런식으로 사용할 수 있는 매소드들이있는데 참고!(알아두면 만이 유용합니다.)
# print(str_test) # 위에서 여러가지 작업을 했지만 str_test는 변경되지 않았습니다. str_test는 변경하지 않았기 때문에 변경하고 다시 str_test에 넣어서 사용해야합니다. 물론 바로 사용해도 됩니다.
# str_test  = str_test.upper()
# print(str_test)
# # print(dir(list_test))
# # print(dir(dict_test))
# # 
# print(dir(wb)) # 많이 출력되므로 구글에서 찾아서 사용하든가아. 출력된 이름을 유츄하여 사용할 것을 찾아도 됩니다.
# Sheet1_sheet = wb["TEST"]
#  # pandas랑은 달리 시트를 직접 불러와서 사용합니다. # 변수명에 어떤파일, 어떤 형태인지 알려주는게 좋습니다.
# print(Sheet1_sheet)
# print(dir(Sheet1_sheet))
# print(Sheet1_sheet.views)

# print(Sheet1_sheet['A3'].value)
# 실패 다시 판다스로,, openpyxl은 전체 데이터를 보여주지 않네여...