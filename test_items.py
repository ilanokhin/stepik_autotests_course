from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time


class TestsForStepik():
    def test_add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        wait = WebDriverWait(browser, 60)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        try:
            addtobasket_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
            assert True
        except NoSuchElementException:
            assert False, "Add to basket button is missing"

        sleep(30)
