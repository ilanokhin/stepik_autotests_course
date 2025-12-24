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

        link = "https://suninjuly.github.io/execute_script.html"

        driver = webdriver.Chrome()
        driver.get(link)
        wait = WebDriverWait(driver, 90)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        input_value = driver.find_element(By.CSS_SELECTOR, '#input_value')
        driver.execute_script("return arguments[0].scrollIntoView(true);", input_value)
        x = int(input_value.text)

        print(x)
        print(calc(x))

        text_field = driver.find_element(By.CSS_SELECTOR, '#answer')
        driver.execute_script("return arguments[0].scrollIntoView(true);", text_field)
        text_field.send_keys(str(calc(x)))

        checkbox = driver.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
        driver.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()

        radiobutton = driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
        driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
        radiobutton.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn[type="submit"]')
        driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()


    finally:
        sleep(5)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    main()
