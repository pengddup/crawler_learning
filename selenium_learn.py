from selenium import webdriver
import time

driver =webdriver.Chrome()
#实例化这个驱动对象

driver.get('https://bbs.badmintoncn.com/member.php?mod=logging&action=login')
#用实例化的浏览器打开这个网页，这个是中羽的
time.sleep(5)

zhongyuID = driver.find_element_by_name('username')
#找到中羽用户名

zhongyuID.send_keys('斯沃德')
#输入用户名

zhongyuPW = driver.find_element_by_name('password')
#找到密码框
zhongyuPW.send_keys('jian5616')
#输入用户名

zhongyuYZ =driver.find_element_by_name('seccodeverify')

zhongyuYZ.send_keys('CWFC')

anniu = driver.find_element_by_name('loginsubmit')

anniu.click()

