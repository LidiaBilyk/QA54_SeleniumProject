from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"
#        test1@gg.com
#         Aa_1234!

def test_login():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        element = driver.find_element(By.NAME, 'email')
        assert element.is_displayed()

    finally:
        driver.quit()


def test_registration_button_is_displayed():
    driver = webdriver.Chrome()
    try:
        driver.get(URL)
        button = driver.find_element(By.XPATH, "//button[text()='Registration']")
        assert button.is_displayed()

    finally:
        driver.quit()
