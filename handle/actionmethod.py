#from pykeyboard import PyKeyboard
import allure
from selenium.webdriver.support import expected_conditions
import os
#import pyperclip
#from pymouse import PyMouse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from log.user_log import User_Log
from base.find_element import Findelement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

log = User_Log().get_log()
close_log = User_Log().close_handler()
class ActionMethod:
    #打开浏览器
    def open_browser(self,browser,*args):
        if browser == '谷歌':
            self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
            #log.info('获取浏览器驱动类型%s'%browser)
            #User_Log().close_handler()
        elif browser == '火狐':
            self.driver = webdriver.Firefox()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            return None
    #输入URL
    def send_url(self,url,*args):
        self.driver.get(url)
    #定位元素
    def FindElement(self,key,node):
        try:
            get_element = Findelement(self.driver)
            element = get_element.get_value(key,node)
            return element
        except:
            return None

    #输入元素
    @allure.step(title='输入数据')
    def send_value(self,key,value,node):

        find_element = self.FindElement(key,node)
        #time.sleep(10)
        find_element.send_keys(value)
        log.info('元素输入%s' % value)
        User_Log().close_handler()
        #print(value)
    #点击元素
    def click_element(self,key,node):
        #隐式等待
        self.driver.implicitly_wait(5)
        self.FindElement(key,node).click()

    #获取title
    def get_title(self):
        return self.driver.title
    #等待响应
    def sleep_time(self,sleep_time):
        time.sleep(sleep_time)

    #下拉框获取元素
    def get_select_value(self,key,value,node):
        element = self.FindElement(key,node)

        loc = (By.XPATH,value)
        #self.driver.switch_to_frame(loc)
        #显式等待
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(loc))
        #time.sleep(5)
        #print(value)
        element.find_element_by_xpath(value).click()

    def get_select_value1(self,key,value,node):
        element = self.FindElement(key,node)
        loc = (By.PARTIAL_LINK_TEXT,value[2])
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(loc))
        #time.sleep(5)
        #print(value)
        element.find_element_by_partial_link_text(value[2]).click()

    def screenshot(self):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        filename = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/Image/' + now_time + '预期失败.png')
        self.driver.save_screenshot(filename)

    #def upload_file(self,key,value,node):
        #self.FindElement(key, node).send_keys(value)

    '''#文件上传
    def upload_file(self,key,file):
        k = PyKeyboard()
        m = PyMouse()
        filepathheard = '/'
        k.press_keys(['Command', 'Shift', 'G'])
        x_dim, y_dim = m.screen_size()
        m.click(x_dim // 2, y_dim // 2, 1)
        # 复制文件路径开头的斜杠/
        pyperclip.copy(filepathheard)
        # 粘贴斜杠/
        k.press_keys(['Command', 'V'])
        # 拼接完整路径
        #fi = get_file_path(file)
        # 输入文件全路径进去
        k.type_string(file)
        k.press_key('Return')
        time.sleep(2)
        k.press_key('Return')
        time.sleep(2)'''

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()


