import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()




def test_login(driver):

    element = driver.find_element(By.NAME, 'email')
    assert element.is_displayed()

def test_registration_button_is_displayed(driver):

    button = driver.find_element(By.XPATH, "//button[text()='Registration']")
    assert button.is_displayed()

def test_login_success(driver):
    driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("test1@gg.com")
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("Aa_1234!")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()


