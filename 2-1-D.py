from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math


def main():
    try:
        # webdriver_path = "C:\\yandexdriver\\yandexdriver.exe"
        # service = Service(webdriver_path)
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
        # driver = webdriver.Chrome(service=service, options=options)

        link = "http://suninjuly.github.io/get_attribute.html"

        driver = webdriver.Chrome()
        driver.get(link)
        wait = WebDriverWait(driver, 90)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        treasure = driver.find_element(By.CSS_SELECTOR, '#treasure')
        valuex = treasure.get_attribute('valuex')

        print(valuex)

        x = int(valuex)

        print(x)
        print(calc(x))

        text_field = driver.find_element(By.CSS_SELECTOR, '#answer')
        text_field.send_keys(str(calc(x)))

        checkbox = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
        checkbox.click()

        radiobutton = driver.find_element(By.CSS_SELECTOR, '#robotsRule')
        radiobutton.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn[type="submit"]')
        submit_button.click()


    finally:
        sleep(5)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    main()
