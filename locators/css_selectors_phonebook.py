from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://telranedu.web.app/login")
    # "https://icarro-v1.netlify.app/search?page=0&size=10"

    # by TAG_NAME
    div = driver.find_elements(By.TAG_NAME, "div")
    div2 = driver.find_element(By.CSS_SELECTOR, "div")
    # div3 = driver.find_element(By.XPATH, "div")
    print(len(div))

    h1 = driver.find_element(By.TAG_NAME, "h1")
    h1_2 = driver.find_element(By.CSS_SELECTOR, "h1")

    input1 = driver.find_element(By.TAG_NAME, "input")
    input2 = driver.find_element(By.CSS_SELECTOR, "input")

    a_list = driver.find_elements(By.TAG_NAME, "a")
    a_list_1 = driver.find_element(By.CSS_SELECTOR, "a")
    print(len(a_list))

    #by class
    container = driver.find_element(By.CLASS_NAME, "container")
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")

    nav_bar = driver.find_elements(By.CLASS_NAME, "active")
    nav_bar_1 = driver.find_elements(By.CSS_SELECTOR, ".active")

    print(len(nav_bar))
    print(len(nav_bar_1))

    login_1 = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_1_1 = driver.find_element(By.CSS_SELECTOR, ".login_login__3EHKB")

    # by ID
    root = driver.find_element(By.ID, "root")
    root_1 = driver.find_element(By.CSS_SELECTOR, "#root")
    root_2 = driver.find_elements(By.ID, "root")

    # # by attribute
    # name = driver.find_element(By.CSS_SELECTOR,'input[name="email"]')
    # email = driver.find_element(By.CSS_SELECTOR,"input[name=\"email\"]")
    #
    # subtitle = driver.find_element(By.CSS_SELECTOR,'[class*="Type your data and hit Yalla!"]')
    # start_sub = driver.find_element(By.CSS_SELECTOR,"")
    #


    #linkText @ partialLinkTest
    home = driver.find_element(By.LINK_TEXT, "HOME")
    home1 = driver.find_element(By.PARTIAL_LINK_TEXT, "OME")



    div3 = driver.find_element(By.XPATH, "//div")

    h1_3 = driver.find_element(By.XPATH, "//h1")

    input1_1 = driver.find_element(By.XPATH, "//input")

    a_list_2 = driver.find_elements(By.XPATH, "//a")

    container_2 = driver.find_element(By.XPATH, "//*[@class='container']")

    nav_bar_2 = driver.find_element(By.XPATH, "//*[@class = 'active']")

    login_2 = driver.find_element(By.XPATH, "//*[@class = 'login_login__3EHKB']")

    root_3 = driver.find_element(By.XPATH, "//*[@id = 'root']")

    email_xpath = driver.find_element(By.XPATH, "//input[@name = 'email']")

    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login1_button = driver.find_element(By.XPATH, "//*[contains(text(),'Login')]")

    input_3 = driver.find_element(By.XPATH, "//input[@placeholder='Email']")

    #starts CSS
    input_4 = driver.find_element(By.CSS_SELECTOR, "[placeholder^='Em']")
    #starts XPath
    input_4_1 = driver.find_element(By.XPATH, "//*[starts-with(@placeholder,'Em')]")
    #ends CSS
    input_4_2 = driver.find_element(By.CSS_SELECTOR, "[placeholder$='il']")
    #ends (contains) XPath
    input_4_3 = driver.find_element(By.XPATH, "//*[contains(@placeholder,'il')]")
    #middle CSS
    input5 = driver.find_element(By.CSS_SELECTOR, "[placeholder *= 'ai']")
    #middle (contains) XPath
    input_5_1 = driver.find_element(By.XPATH, "//*[contains(@placeholder,'il')]")


finally:
    driver.quit()