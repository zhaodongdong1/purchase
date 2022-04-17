#读取ini配置文件的模块
import configparser
import os
import unittest

class Read_INI():
    def __init__(self,filename='',node=''):
        fileaddress = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'/config/'+'LocalElement.ini')

        #print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
        if filename == '':
            self.filename = fileaddress
        else:
            self.filename = filename

        if node == '':
            self.node = 'recodeElement'
        else:
            self.node = node

        #self.cf = self.read_inidata()
        #self.cf.read(self.filename)


    def read_inidata(self,key):
        cf = configparser.ConfigParser()
        cf.read(self.filename)
        data = cf.get(self.node,key)
        return data
'''
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data'''

'''
    def read_ini(self,key):
        cf = configparser.ConfigParser()
        cf.read(self.filename)
        data = cf.get(self.node,key)
        return data'''

if __name__ == '__main__':
    rea_data = Read_INI()
    print(rea_data.read_inidata('username'))