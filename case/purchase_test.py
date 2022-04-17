#coding=utf-8
from util.read_excel import ReadExcelData
from handle.actionmethod import ActionMethod
import os
from log.user_log import User_Log
import unittest
from selenium import webdriver
log = User_Log().get_log()
close_log = User_Log().close_handler()
class Test_Keyword_Purchasecase(unittest.TestCase):
    #def setUp(self):
        #self.driver = webdriver.Chrome()
        #self.action_method = ActionMethod()
    #def tearDown(self):
        #ActionMethod().close_browser()

    def save_img(self, test_method):
        self.driver = webdriver.Chrome()
        #失败截图方法（必须要定义在class中)
        #root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
        #img_path = root_dir + '/img'
        #self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, test_method))
        filename = os.path.join(
            os.path.abspath(os.path.dirname(__file__)) + '/Img')
        self.driver.save_screenshot(filename+'/%s.png'%test_method)

    #@BeautifulReport.add_test_img('点击资产模块')
    def test_run_main(self):
        self.action_method = ActionMethod()
        caseaddres = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/config/' + 'keywords.xls')
        handle_excel = ReadExcelData(caseaddres)
        #handle_excel = ReadExcelData('/Users/zhaodongdong/PycharmProjects/purchase/config/keywords.xls')
        case_lines = handle_excel.get_lines()
        if case_lines is not None:
            for i in range(1,case_lines):
                module_name = handle_excel.get_col_value(i,1)
                is_run = handle_excel.get_col_value(i,2)
                handle = handle_excel.get_col_value(i,3)
                log.info('配置文件获取：%s->%s-->%s'%(is_run,module_name,handle))
                User_Log().close_handler()
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i,4)
                    nodeelement = handle_excel.get_col_value(i,5)
                    handle_element = handle_excel.get_col_value(i,6)
                    send_data = handle_excel.get_col_value(i,7)
                    #print(send_data)
                    except_result_method = handle_excel.get_col_value(i,8)
                    except_result_value = handle_excel.get_col_value(i,9)
                    self.run_method(method, handle_element, send_data, nodeelement)

                    '''try:
                        self.run_method(method,handle_element,send_data,nodeelement)
                    except Exception as e:
                        self.save_img('Keyword_Purchasecase_test_run_main')
                        self.action_method.close_browser()
                        break'''
                    if except_result_value != '':
                        except_value = except_result_value.split('=')
                        if except_value[0] == 'text':
                            data = self.run_method(except_result_method)
                            if except_value[1] in data:
                                handle_excel.write_value(i,10,'pass')
                            else:
                                handle_excel.write_value(i, 10, 'fail')
                        elif except_value[0] == 'element':
                            self.run_method(except_result_method,except_value[1])
                            #self.action_method.FindElement()
                            print(except_value[1])
                            try:
                                self.action_method.click_element(except_value[1])
                                handle_excel.write_value(i,10,'pass')
                            except:
                                handle_excel.write_value(i, 10, 'fails')
                                self.action_method.screenshot()

                    else:
                        handle_excel.write_value(i, 10,'%s预期结果为空'%handle)

    #@BeautifulReport.add_test_img('点击资产模块')
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
    run_test = Test_Keyword_Purchasecase()
    run_test.test_run_main()