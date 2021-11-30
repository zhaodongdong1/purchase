from BeautifulReport import BeautifulReport
import os
from handle.handle_email import Send_Email
import unittest
import time


if __name__ == '__main__':
    email = Send_Email()
    report_file = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'/report/')
    now_time = time.strftime('%Y-%m-%d')
    file_name = now_time
    test_suite = unittest.defaultTestLoader.discover('.', pattern='*test.py')
    result = BeautifulReport(test_suite)
    result.report(filename=now_time, description='测试deafult报告',theme='theme_default', report_dir=report_file)
    #邮件名称正文内容关键字1
    email.sendemali('purchase')





