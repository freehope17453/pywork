from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://cn.bing.com/")
#driver.quit()
#driver.find_element_by_xpath("//input[@id='sb_form_q']").send_keys("李晓鹏")
#driver.find_element_by_xpath("//input[@id='sb_form_go']").click()
driver.find_element_by_id('sb_form_q').send_keys('王博')
driver.find_element_by_id('sb_form_go').click()
#driver.find_element_by_xpath("//input[@id='sb_form_go']").click()
