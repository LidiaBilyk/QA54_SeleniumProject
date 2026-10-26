from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/css/css_table.asp")
    mexico = driver.find_element(By.CSS_SELECTOR, "#customers tr:nth-child(4)")

    mexico1 = driver.find_element(By.CSS_SELECTOR, "#customers tr:nth-child(4)>td:nth-child(3)")
    assert mexico1.text == "Mexico"

    italy = driver.find_element(By.CSS_SELECTOR, "#customers tr:last-child")
    item1 = driver.find_element(By.CSS_SELECTOR, "#customers tr:first-child")
finally:
    driver.quit()