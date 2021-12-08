from selenium import webdriver
import time

web = webdriver.Chrome()

#Nhap link docs
web.get('linkdocs')


time.sleep(5)


#Nhap xpath cau tra loi (F12 - Sao chep xpath)
radioButtonPeriod = web.find_element_by_xpath('xpath')
radioButtonPeriod.click()

radioButtonPeriod = web.find_element_by_xpath('xpath')
radioButtonPeriod.click()

radioButtonPeriod = web.find_element_by_xpath('xpath')
radioButtonPeriod.click()



#Nhap xpath nui gui (F12 - Sao chep xpath)
sendButton = web.find_element_by_xpath('xpath')
sendButton.click()


