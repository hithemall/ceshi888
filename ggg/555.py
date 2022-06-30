from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.ais.cn")
driver.maximize_window()
sleep(3)
action = ActionChains(driver)
#CSS定位
driver.find_element_by_css_selector("[ class ='login mr25 fs12 hand loginBtn']").click()

driver.find_element_by_css_selector("[placeholder='请输入手机号码/邮箱账号']").send_keys("17353009201")
driver.find_element_by_css_selector("[placeholder='请输入密码']").send_keys("abc123456")
driver.find_element_by_css_selector("[class='layui-btn comfirmBtn']").click()
sleep(2)
#driver.find_element_by_css_selector("[class='vMiddle inlineBlock c-eb8 pl5 pr5 nickname']").click()


action.move_to_element(driver.find_element_by_css_selector("[class='vMiddle inlineBlock c-eb8 pl5 pr5 nickname']")).perform()
sleep(2)
driver.find_element_by_css_selector("[class='inlineBlock vMiddle fBlod c-333 signOut']").click()

#driver.quit()
