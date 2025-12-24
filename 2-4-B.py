from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import os


def main():
    # webdriver_path = "C:\\yandexdriver\\yandexdriver.exe"
    # service = Service(webdriver_path)
    # options = webdriver.ChromeOptions()
    # options.binary_location = "C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
    # driver = webdriver.Chrome(service=service, options=options)

    driver = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"

    try:
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), "$100"))

        book_button = driver.find_element(By.CSS_SELECTOR, '.btn#book')
        book_button.click()
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        input_value = driver.find_element(By.CSS_SELECTOR, '#input_value')
        x = int(input_value.text)

        print(x)
        print(calc(x))

        text_field = driver.find_element(By.CSS_SELECTOR, '#answer')
        text_field.send_keys(str(calc(x)))

        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn[type="submit"]')
        submit_button.click()

    finally:
        sleep(5)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    main()
