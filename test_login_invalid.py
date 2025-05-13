from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)


    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("wrongUser")
    password_input.send_keys("wrongPass")
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)


    error_message = driver.find_element(By.ID, "flash")
    if "invalid" in error_message.text.lower():
        print("Test Başarılı: Hata mesajı görüntülendi.")
    else:
        print("Test Başarısız: Hata mesajı görüntülenmedi.")
finally:

    driver.quit()
