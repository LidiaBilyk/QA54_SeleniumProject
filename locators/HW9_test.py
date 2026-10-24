from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemoWebShopLocators:

    def setup_class(self):
        # Инициализация браузера на уровне класса
        self.driver = webdriver.Chrome()
        self.driver.get("https://demowebshop.tricentis.com/")

    def test_find_elements_strategies(self):
        # Внутри метода обращаемся к драйверу через self.driver

        # --- 1. Поиск по ID ---
        search_box = self.driver.find_element(By.ID, "small-searchterms")
        search_box_css = self.driver.find_element(By.CSS_SELECTOR, "#small-searchterms")

        flyout_cart = self.driver.find_element(By.ID, "flyout-cart")
        flyout_cart_css = self.driver.find_element(By.CSS_SELECTOR, "#flyout-cart")

        # --- 2. Поиск по NAME ---
        search_input_name = self.driver.find_element(By.NAME, "q")
        search_input_css = self.driver.find_element(By.CSS_SELECTOR, "input[name='q']")

        newsletter = self.driver.find_element(By.NAME, "NewsletterEmail")
        newsletter_css = self.driver.find_element(By.CSS_SELECTOR, 'input[name="NewsletterEmail"]')

        # --- 3. Поиск по CLASS_NAME ---
        register = self.driver.find_element(By.CLASS_NAME, "ico-register")
        register_css = self.driver.find_element(By.CSS_SELECTOR, ".ico-register")

        login = self.driver.find_element(By.CLASS_NAME, "ico-login")
        login_css = self.driver.find_element(By.CSS_SELECTOR, ".ico-login")

        logo = self.driver.find_element(By.CLASS_NAME, "header-logo")
        logo_css = self.driver.find_element(By.CSS_SELECTOR, ".header-logo")

        # --- 4. Поиск только по CSS_SELECTOR (комбинации и сложные селекторы) ---
        subscribe_btn = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Subscribe"]')
        poll_block = self.driver.find_element(By.CSS_SELECTOR, '.block-poll')

        # Поиск списка элементов
        top_menu_items = self.driver.find_elements(By.CSS_SELECTOR, "ul.top-menu > li")

        # Ваши принты для отладки и терминала (запускать с флагом -s)
        print("\nУспешно найдено 10 различных элементов!")
        print(f"Количество пунктов в верхнем меню: {len(top_menu_items)}")

        # Обязательные проверки для валидности теста
        assert search_box is not None, "Критическая ошибка: Поле поиска отсутствует на странице!"
        assert len(top_menu_items) == 7, f"Ожидалось 7 пунктов меню, но найдено {len(top_menu_items)}"

    def teardown_class(self):
        # Гарантированное освобождение ресурсов
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    import pytest
    pytest.main(["-s", __file__])