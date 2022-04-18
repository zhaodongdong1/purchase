import allure

from util.readini import Read_INI
import time
import os
from selenium import webdriver
from log.user_log import User_Log
log = User_Log().get_log()

data = Read_INI().read_inidata('212222')
if data is not None:
    by = data.split('>')[0]
    value = data.split('>')[1]
    print(by)