#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 16/11/8 12:09
# @Author     : Zhangxy
# @File       : 001baiduSearch.py
# @Software   : PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import selenium

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://localhost:6008")
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').send_keys('zuikaku22195068')
driver.find_element_by_class_name('btn-danger').click()
# driver.implicitly_wait(5)
# driver.find_element_by_link_text(u"Query管理").click()
#
# time.sleep(5)
# checkboxs = driver.find_elements_by_name('queryCheck')
# for checkbox in checkboxs:
#     if checkbox.get_attribute('type') == 'checkbox':
#         checkbox.send_keys(selenium.webdriver.common.keys.Keys.SPACE)
#
# driver.execute_script('$("#thresholdSet").show()')
#
# driver.execute_script('$("#batchtest").click()')
# driver.implicitly_wait(5)
# upload = driver.find_element_by_id('selectfile')
# upload.send_keys('C:\\fakepath\\TainingData.csv')
# driver.find_element_by_link_text(u"バッチテスト実行").click()

# driver.find_element_by_id('iconofselectfile').click()

# driver.quit()