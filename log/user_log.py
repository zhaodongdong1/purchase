import logging
import os
import datetime
class User_Log():
    def __init__(self):
        #创建日志收集器对象
        self.loger = logging.getLogger()
        #设置收集器对象收集日志等级
        self.loger.setLevel(logging.INFO)
        #被调用后清空已经存在的handler
        #self.loger.handlers.clear()
        #控制台输出日志
        #创建数据流输出控制台渠道
        #self.consle = logging.StreamHandler()
        #指定log文件路径
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
        file_name = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/logs/'+nowtime+'test.log')
        #创建数据流输出文件渠道
        self.file_handle = logging.FileHandler(file_name)
        #创建数据流输出log文件渠道
        #filename = os.path.abs
        #设置日志格式，asctime时间，filename文件名称，levelname日志等级，module日志模块，funcName调用方法名称，message日志内容
        formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(module)s %(funcName)s----> %(message)s')
        #格式化文件渠道日志格式
        self.file_handle.setFormatter(formatter)
        #新增handler时判断是否已经存在handler
        if not self.loger.handlers:
            # 收集器中添加输出渠道
            #self.loger.addHandler(self.consle)
            self.loger.addHandler(self.file_handle)

    def get_log(self):
        return self.loger
    def close_handler(self):
        #不好使self.loger.handlers.clear()
        self.file_handle.close()
        self.loger.removeHandler(self.file_handle)

if __name__ == '__main__':
    user = User_Log()
    logger = user.get_log()
    logger.info('testss')

