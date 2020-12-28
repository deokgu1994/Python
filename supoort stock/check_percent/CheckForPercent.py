import os
import sys
import time

import requests
from PyQt5 import QtCore, QtGui, QtWidgets, QtCore
from bs4 import BeautifulSoup

def is_print(text):
    if True:
        print("{}".format(text))

# TODO : how to using movetothread?

def getRateOfFluctuation(now_price : str, get_price : str, commission_rate = 0.03):
    # FIXME : add commission_rate
    now_price = int(now_price.replace(",", ""))
    get_price = int(get_price.replace(",", ""))

    rate = "%0.2f" % ((now_price-get_price)/get_price * 100) + "%"
    return rate


class oF_OutPutPercent(QtCore.QThread):
    now_price_siganl = QtCore.pyqtSignal(str)
    is_run = False
    def __init__(self, parent, company_code, buy_price):
        super(oF_OutPutPercent, self).__init__()
        self.parent = parent
        self.company_code = company_code
        self.buy_price = buy_price
        
        self.is_second = False
        pass
    
    def run(self,):
        # FIXME : Let's Check time 
        # FIXME : Let's dieffernet while 1
        # TODO : first data out -> delay -> out 
        is_print("start output")
        self.is_run = True
        while 1:
            if self.is_run:
                start_time = time.time()

                # delay total 5s so i'm using to "5- (time.time() - start_time)" this time delay
                
                if self.is_second:
                    # delay_time = round((5 - (time.time()-start_time)) * 1000)
                    # if delay_time > 0:
                    #     is_print(delay_time)
                    # i think always 1.5s so 1.5 slepp -> 3s
                    self.msleep(1500)
                
                # Buffering... 
                url = "https://finance.naver.com/item/main.nhn?code=" + self.company_code
                result = requests.get(url)
                bs_obj = BeautifulSoup(result.content, "html.parser")
                
                no_today = bs_obj.find("p", {"class": "no_today"}) # 태그 p, 속성값 no_today 찾기
                blind = no_today.find("span", {"class": "blind"}) # 태그 span, 속성값 blind 찾기
                # 1.5s
                now_price = blind.text

                self.now_price_siganl.emit(now_price)
                self.is_second =True
            else:
                break
        self.is_second = False
        self.is_run = False


class oF_StockInfo(QtWidgets.QWidget):
    """
        below using oF_StockInfo -> sif

    """
    delete_stockinfo = QtCore.pyqtSignal(int)
    def __init__(self, ):
        super(oF_StockInfo, self).__init__()
        is_print("new stock info")
        self.sif_main_hlayout = QtWidgets.QHBoxLayout()

        self.index_num_label = QtWidgets.QLabel()
        # self.index_num_label.setMinimumSize(1,1)
        self.index_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sif_main_hlayout.addWidget(self.index_num_label, 1)
        
        # self.stock_name_edit = QtWidgets.QLineEdit("003000")
        self.stock_name_edit = QtWidgets.QLineEdit()
        # self.stock_name_edit.setMinimumWidth()
        self.sif_main_hlayout.addWidget(self.stock_name_edit, 2)

        # self.stock_buy_price_edit = QtWidgets.QLineEdit("100")
        self.stock_buy_price_edit = QtWidgets.QLineEdit()
        # self.stock_buy_price_edit.setMinimumSize(10,10)
        self.sif_main_hlayout.addWidget(self.stock_buy_price_edit, 2)

        self.stock_now_price_label = QtWidgets.QLabel()
        self.sif_main_hlayout.addWidget(self.stock_now_price_label, 3)

        self.stock_price_percent_label = QtWidgets.QLabel()
        self.sif_main_hlayout.addWidget(self.stock_price_percent_label, 3)

        self.stock_check_start_pushbutton = QtWidgets.QPushButton('>')
        self.stock_check_start_pushbutton.clicked.connect(self.oF_startCheck)
        self.sif_main_hlayout.addWidget(self.stock_check_start_pushbutton, 1)

        self.stock_delete_pushbutton = QtWidgets.QPushButton("-")
        self.stock_delete_pushbutton.clicked.connect(self.oF_sotckDelete)
        self.sif_main_hlayout.addWidget(self.stock_delete_pushbutton)

        self.setLayout(self.sif_main_hlayout)

    def oF_startCheck(self,):
        if self.stock_name_edit.text() == "":
            # FIXME : Let's use different sentences to "information"
            QtWidgets.QMessageBox.information( self, "More Infomation"
                            ,"Please Insert Comapany Name")
            return 
        if self.stock_buy_price_edit.text() == "":
            # FIXME : Let's use different sentences to "information"
            QtWidgets.QMessageBox.information( self, "More Infomation"
                            ,"Please Insert Buy Prices")
            return 


        
        self.output_mian_thread = oF_OutPutPercent(self
                                            , self.stock_name_edit.text() # company code
                                            , self.stock_buy_price_edit.text() # price
                                            )
        
        print(type(self.output_mian_thread.now_price_siganl))
        print(dir(self.output_mian_thread.now_price_siganl))
        
        self.output_mian_thread.now_price_siganl.connect(self.oF_changePriceAndPercent)
        self.stock_check_start_pushbutton.setText("=")
        self.output_mian_thread.start()
        
        # output_timer.timeout.connect(lambda : self.output_mian_thread.run_carwling())

    def oF_sotckDelete(self,):
        if hasattr(self, "ouput_main_thread"):
            if self.output_mian_thread.is_run:
                self.output_mian_thread.is_run = False

        self.delete_stockinfo.emit(int(self.index_num_label.text()))

    @QtCore.pyqtSlot(str)
    def oF_changePriceAndPercent(self, arg1):
        # FIXME : add commission rate
        self.stock_now_price_label.setText(arg1)
        self.stock_now_price_label.update()

        self.stock_price_percent_label.setText(str(getRateOfFluctuation(arg1, self.stock_buy_price_edit.text())))
        self.stock_price_percent_label.update()
        

class oF_StockListVLayout(QtWidgets.QVBoxLayout):
    """
        below using StockViewWidget -> svw

        input data : stock name, buy price 
        output data : now price, percent()
    """
    stock_index = 0
    def __init__(self,parent):
        super(oF_StockListVLayout, self).__init__()
        self.parent = parent
        self.stock_layout_list = list()
        self.setSpacing(0)
        pass

    @QtCore.pyqtSlot()  
    def oF_addStockView(self, ):
        is_print("start addStockView")
        # numbering start 1 
        oF_StockListVLayout.stock_index += 1
        
        # add Stock info
        stock_info = oF_StockInfo()

        stock_info.delete_stockinfo.connect(self.oF_deletStockView)
        stock_info.index_num_label.setText(str(oF_StockListVLayout.stock_index))
        stock_info.update()

        self.addWidget(stock_info)
        # numbering start 0
        self.stock_layout_list.append(stock_info)
        self.update()
        pass

    @QtCore.pyqtSlot(int)
    def oF_deletStockView(self, index):
        print('dlelete stock view')
        if oF_StockListVLayout.stock_index == 0:
            is_print("indoex 0")
            return
        # numbering start 0
        self.removeWidget(self.stock_layout_list[index -1])
    
        self.stock_layout_list[index-1].deleteLater()
        self.stock_layout_list[index-1] = None
        
        oF_StockListVLayout.stock_index -= 1

        self.oF_reNumberrring(index)
        self.update()

    def oF_reNumberrring(self, index):
        temp_stock_lyaout_list = list()
        print(f"-----check sotkc_index {oF_StockListVLayout.stock_index}")
        for index in range(1, oF_StockListVLayout.stock_index + 1):
            print(f"Check for in index {index}")
            print(f"---check layout list {self.stock_layout_list[index]}")
            if self.stock_layout_list[index-1] is None:
                stock_info = self.stock_layout_list[1]
                self.stock_layout_list = self.stock_layout_list[2:]
            else:
                stock_info = self.stock_layout_list[0]
                self.stock_layout_list = self.stock_layout_list[1:]
            stock_info.index_num_label.setText(str(index))
            temp_stock_lyaout_list.append(stock_info)

        self.stock_layout_list = temp_stock_lyaout_list
        print(f"check {self.stock_layout_list}")
        
class oF_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(oF_MainWindow, self).__init__()

        self.stocks_list= []

        self.stocks_VLayout = oF_StockListVLayout(self)
        self.oF_createDockWidgets()

        temp_in_vlayout_Widget = QtWidgets.QWidget()
        temp_in_vlayout_Widget.setLayout(self.stocks_VLayout)
        self.setCentralWidget(temp_in_vlayout_Widget)

        # txt 파일 만들어서 그거 끌때 저장하고 킬때 불러 올 수 있도록 만들기
        # self.oF_readPortfolilo("")

        # self.setWindowTitle("Stock Check Percent - OF")
    
    def oF_createDockWidgets(self,):
        """
            create Dock Widgets
        """
        # SettingDock Widget
        dock = QtWidgets.QDockWidget("Setting", self)
        dock.setAllowedAreas(QtCore.Qt.TopDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)
        self.setting_DcokWidgets = oF_SettingDockWidget()

        self.setting_DcokWidgets.add_pushbutton.clicked.connect(self.stocks_VLayout.oF_addStockView)
        # self.setting_DcokWidgets.delet_pushbutton.clicked.connect(self.stocks_VLayout.oF_deletStockView)       

        dock.setWidget(self.setting_DcokWidgets)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock)
        # end 

        # Dock widget add here

    # def __close


class oF_SettingDockWidget(QtWidgets.QWidget):
    """
        below using SettingDockWidget -> sdw
         
        This setting sotck add, delet and commission rate
    """
    def __init__(self,):
        super(oF_SettingDockWidget, self).__init__()
        self.sdw_main_HLayout = QtWidgets.QHBoxLayout()

        # + button -> add stock view 
        self.add_pushbutton  = QtWidgets.QPushButton("+")
        self.sdw_main_HLayout.addWidget(self.add_pushbutton)

        # - button -> delet stock view(not chose -> bottom delet)
        self.delet_pushbutton = QtWidgets.QPushButton("-")
        self.sdw_main_HLayout.addWidget(self.delet_pushbutton)

        self.setLayout(self.sdw_main_HLayout)

 
# url = "https://finance.naver.com/item/main.nhn?code=263750"
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
 
# no_today = bs_obj.find("p", {"class": "no_today"}) # 태그 p, 속성값 no_today 찾기
# blind = no_today.find("span", {"class": "blind"}) # 태그 span, 속성값 blind 찾기
# now_price = blind.text
 
# print(now_price)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    oF_check_for_percent = oF_MainWindow()
    oF_check_for_percent.resize(500,50)
    oF_check_for_percent.show()
    sys.exit(app.exec_())