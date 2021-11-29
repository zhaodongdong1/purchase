import smtplib,time,os
from email.mime.text import MIMEText
from email.utils import formataddr,parseaddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import yaml
class Send_Email(object):

    #从配置文件中加载获取email的相关信息
    def load_emil_setting(self):
        #yaml文件的绝对路径
        file_tree = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config/' + 'eamail_data.yaml')
        #打开yaml文件
        data_file = open(file_tree,"r")
        #加载打开的yaml文件，源码中load有两个参数，所以调用时要传Loader=yaml.FullLoader
        datas = yaml.load(data_file,Loader=yaml.FullLoader)
        data_file.close()
        #print(datas)
        return (datas['emailname'],datas['password'],datas['toeamil'],datas['title'])
    #print(load_emil_setting())
    def sendemali(self,modle,filepath=''): #发送email
        if filepath == '':
            filepath = '/Users/zhaodongdong/PycharmProjects/purchase/report/2021-11-27.html'
        else:
            filepath = filepath
        #按顺序获取load_emil_setting函数返回数据
        from_addr,password,mail_to,mail_body=self.load_emil_setting()
        #设置邮件信息
        msg = MIMEMultipart()
        msg['Subject'] = '%s自动化测试报告'%modle    #邮件主题
        msg['From'] ='purchase测试报告'            #发送者名称
        msg['To'] = mail_to                           #接收者地址
        msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')        #发送时间

        #设置附件
        #att = MIMEText(open(r'%s'%filepath, 'rb').read(), 'base64', 'utf-8')   #打开文件
        att = MIMEText(filepath, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'  #用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件
        att["Content-Disposition"] = 'attachment; filename="2021-11-27.html"'  #文件描述，filename为定义文件名
        # 邮件正文
        txt = MIMEText("这是%s测试报告的邮件，详情见附件"%modle, 'plain', 'gb2312')

        # 将正文和附件加载到邮件中
        msg.attach(txt)
        msg.attach(att)

        # 发送邮件
        smtp = smtplib.SMTP()
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器地址
        server.login(from_addr, password)  # 登录邮箱，qq邮箱密码为授权码
        server.sendmail(from_addr, mail_to, msg.as_string())  # 发送邮件
        server.quit()


if __name__ == '__main__':
    Send_Email().sendemali('集采')
#sendemali('/Users/zhaodongdong/PycharmProjects/purchase/report/2021-11-27.html')