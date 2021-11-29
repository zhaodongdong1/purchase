from util.readini import Read_INI
import time
import os
from selenium import webdriver
from log.user_log import User_Log
log = User_Log().get_log()

class Findelement():

    def __init__(self, driver):
        self.driver = driver

    def get_value(self,key,node='',filename=''):
        data = Read_INI(filename,node).read_inidata(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        log.info('调用ini文件的key为%s'%key)
        User_Log().close_handler()
        try:
            if by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'class':
                return self.driver.find_element_by_class(value)
            else:
                return self.driver.find_element_by_class_name(value)
        except:
            nowtim = time.strftime("%Y-%m-%d %H:%M:%S")
            filename = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Image/' + nowtim + key + '.png')
            self.driver.save_screenshot(filename)
            return None
'''
if __name__ == '__main__':
    qq = Findelement()
    print(qq.get_value('username'))'''