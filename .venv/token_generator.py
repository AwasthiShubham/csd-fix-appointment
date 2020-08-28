from selenium import webdriver
import time

driver =  webdriver.Chrome('D:\\Study\\Automation\\chromedriver_win32\\chromedriver.exe')

driver.get('https://nccurcrbl.setmore.com/')
driver.find_element_by_xpath('//*[@id="close-policy"]').click()
driver.find_element_by_xpath('//*[@id="serviceName_toolTip"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="r83ec1589475304019"]').click()

