from selenium import webdriver
driver = webdriver.Firefox()

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

firstInputField = driver.find_element_by_xpath('//*[@id="sum1"]')
firstInputField.send_keys('2')
secondInputField = driver.find_element_by_xpath('//*[@id="sum2"]')
secondInputField.send_keys('3')
findSumButton = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
findSumButton.click()
