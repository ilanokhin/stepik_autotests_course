from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import os


def main():
    try:
        # webdriver_path = "C:\\yandexdriver\\yandexdriver.exe"
        # service = Service(webdriver_path)
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
        # driver = webdriver.Chrome(service=service, options=options)

        link = "http://suninjuly.github.io/file_input.html"

        driver = webdriver.Chrome()
        driver.get(link)
        wait = WebDriverWait(driver, 90)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        firstname_field = driver.find_element(By.CSS_SELECTOR, '.form-control[name="firstname"]')
        firstname_field.send_keys('Ivan')

        lastname_field = driver.find_element(By.CSS_SELECTOR, '.form-control[name="lastname"]')
        lastname_field.send_keys('Petrov')

        email_field = driver.find_element(By.CSS_SELECTOR, '.form-control[name="email"]')
        email_field.send_keys('ivan@petrov.com')

        current_dir_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir_path, "data.txt")

        filesend = driver.find_element(By.CSS_SELECTOR, '#file')
        filesend.send_keys(file_path)

        print(file_path)

        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn[type="submit"]')
        submit_button.click()

    finally:
        sleep(5)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    main()
