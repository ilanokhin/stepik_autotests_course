from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import math


def main():
    try:
        # webdriver_path = "C:\\yandexdriver\\yandexdriver.exe"
        # service = Service(webdriver_path)
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
        # driver = webdriver.Chrome(service=service, options=options)

        link = "https://suninjuly.github.io/selects1.html"

        driver = webdriver.Chrome()
        driver.get(link)
        wait = WebDriverWait(driver, 90)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        num1 = driver.find_element(By.CSS_SELECTOR, '#num1')
        num2 = driver.find_element(By.CSS_SELECTOR, '#num2')
        sum = (int(num1.text) + int(num2.text))
        print(sum)

        dropbox = driver.find_element(By.CSS_SELECTOR, '#dropdown')
        dropbox.send_keys(str(sum))

        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn[type="submit"]')
        submit_button.click()

    finally:
        sleep(5)
        driver.quit()


if __name__ == '__main__':
    main()
