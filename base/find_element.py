import allure

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
        log.info('调用ini文件的key为%s,data是%s' % (key, data))
        User_Log().close_handler()
        if data is not None:
                by = data.split('>')[0]
                value = data.split('>')[1]
                if by == 'xpath':
                    return self.driver.find_element_by_xpath(value)
                elif by == 'id':
                    return self.driver.find_element_by_id(value)
                elif by == 'class':
                    return self.driver.find_element_by_class(value)
                else:
                    return self.driver.find_element_by_class_name(value)
        else:
            nowtim = time.strftime("%Y-%m-%d %H:%M:%S")
            allure.attach(self.driver.get_screenshot_as_png(), '失败截图,定位方式是%s' % key, allure.attachment_type.PNG)
            filename = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Image/' + nowtim + key + '.png')
            self.driver.save_screenshot(filename)
            return None
'''
if __name__ == '__main__':
    qq = Findelement()
    print(qq.get_value('username'))'''