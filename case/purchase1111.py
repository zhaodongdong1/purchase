from util.read_excel import ReadExcelData
from handle.actionmethod import ActionMethod
import os
from log.user_log import User_Log
from BeautifulReport import BeautifulReport
import unittest
from selenium import webdriver

log = User_Log().get_log()
close_log = User_Log().close_handler()
class Keyword_Purchasecase(unittest.TestCase):
    #def setUp(self):
        #self.driver = webdriver.Chrome()
        #self.action_method = ActionMethod()
    #def tearDown(self):
        #ActionMethod().close_browser()

    def save_img(self, test_method):
        self.driver = webdriver.Chrome()
        #失败截图方法（必须要定义在class中)
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        img_path = root_dir + '/image'
        self.driver.get_screenshot_as_file('%s/%s.png'%(img_path, test_method))

    #@BeautifulReport.add_test_img('点击资产模块')
    def run_main(self):
        self.action_method = ActionMethod()
        caseaddres = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/config/' + 'keywords.xls')
        self.handle_excel = ReadExcelData(caseaddres)
        #handle_excel = ReadExcelData('/Users/zhaodongdong/PycharmProjects/purchase/config/keywords.xls')
        self.case_lines = self.handle_excel.get_lines()


    #@BeautifulReport.add_test_img('点击资产模块')
    def test_run(self):
        if self.case_lines is not None:
            for i in range(1,self.case_lines):
                module_name = self.handle_excel.get_col_value(i,1)
                self.is_run = self.handle_excel.get_col_value(i,2)
                self.handle = self.handle_excel.get_col_value(i,3)
                log.info('配置文件获取：%s->%s-->%s'%(self.is_run,module_name,self.handle))
                User_Log().close_handler()
        #caseaddres = os.path.join(
            #os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/config/' + 'keywords.xls')
        #handle_excel = ReadExcelData(caseaddres)
                if self.is_run == 'yes':
                    method = self.handle_excel.get_col_value(i, 4)
                    nodeelement = self.handle_excel.get_col_value(i, 5)
                    handle_element = self.handle_excel.get_col_value(i, 6)
                    send_data = self.handle_excel.get_col_value(i, 7)
                    # print(send_data)
                    except_result_method = self.handle_excel.get_col_value(i, 8)
                    except_result_value = self.handle_excel.get_col_value(i, 9)
                    try:
                        self.run_method(method, handle_element, send_data, nodeelement)
                    except:
                        self.save_img(self.handle)
                        self.action_method.close_browser()

                    if except_result_value != '':
                        except_value = except_result_value.split('=')
                        if except_value[0] == 'text':
                            data = self.run_method(except_result_method)
                            if except_value[1] in data:
                                self.handle_excel.write_value(i, 10, 'pass')
                            else:
                                self.handle_excel.write_value(i, 10, 'fail')
                        elif except_value[0] == 'element':
                            self.run_method(except_result_method, except_value[1])
                            # self.action_method.FindElement()
                            print(except_value[1])
                            try:
                                self.action_method.click_element(except_value[1])
                                self.handle_excel.write_value(i, 10, 'pass')
                            except:
                                self.handle_excel.write_value(i, 10, 'fails')
                                self.action_method.screenshot()

                    else:
                        self.handle_excel.write_value(i, 10, '%s预期结果为空' % self.handle)


    def run_method(self,method,handle_element='',send_data='',node_element=''):
        method_value = getattr(self.action_method,method)
        if send_data != '' and handle_element != '':
            if str(send_data)[-2:] == '.0':
                result = method_value(handle_element,int(send_data),node_element)
            else:
                result = method_value(handle_element,send_data,node_element)
        elif send_data != '' and handle_element == '':
            if str(send_data)[-2:] == '.0':
                result = method_value(int(send_data))
                #print(int(send_data))
            else:
                result = method_value(send_data)
        elif send_data == '' and handle_element != '':
            #if str(handle_element)[-2:] == '.0':
                #result = method_value(int(handle_element))
            #else:
            result = method_value(handle_element,node_element)
        else:
            result = method_value()
        return result


if __name__ == '__main__':
    run_test = Keyword_Purchasecase()
    run_test.test_run()