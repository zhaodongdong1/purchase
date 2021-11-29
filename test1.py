from base.find_element import Findelement
from selenium import webdriver
class aaa:
    def bb(self):
        self.driver = webdriver.Chrome()
    def b2(self):
        a1 = Findelement()
        a2 = a1.get_value('username')
        print(a2)
        return a2


if __name__ == '__main__':
    aq = aaa
    print(aq.b2)