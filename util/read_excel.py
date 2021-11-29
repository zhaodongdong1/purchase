from xlutils.copy import copy
import xlrd
import os
from log.user_log import User_Log
#log = User_Log().get_log()
#close_log = User_Log().close_handler()
class ReadExcelData():
    def __init__(self,excel_path=None,index=None):
        filename = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/config/' + 'keywords.xls')
        if excel_path == None:
            self.excel_path = filename
        else:
            self.excel_path = excel_path

        if index == None:
            self.index = 0
        else:
            self.index = index

        #打开文件
        self.table = xlrd.open_workbook(self.excel_path)
        #定位sheet页
        self.sheet = self.table.sheets()[self.index]

    #获取文件行数
    def get_lines(self):
        rows = self.sheet.nrows
        if rows >= 1:
            return rows
        else:
            return None

    #遍历行数获取所有数据
    def get_data(self):
        data_case = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(rows):
                #获取i行数据
                col = self.sheet.row_values(i)
                data_case.append(col)
            return data_case
        else:
            return None
    #获取单元格数据,供外部调用某一单元格数据,row是行，col是列
    def get_col_value(self,row,col):
        if self.get_lines() > row:
            data = self.sheet.cell(row,col)
            return data.value
        else:
            return None

    #写入数据
    def write_value(self,row,col,value):
        table_data = copy(xlrd.open_workbook(self.excel_path))
        #get_sheet获取sheet页
        get_sheet_index = table_data.get_sheet(self.index)
        get_sheet_index.write(row,col,value)
        #print(aa)
        table_data.save(self.excel_path)
'''
if __name__ == '__main__':
    run = ReadExcelData()
    print(run.write_value(2,5,123))'''
