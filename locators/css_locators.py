from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://telranedu.web.app/login")

driver.close() #only last atb will be closed
driver.quit() #used to close whole process
