from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def  test_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()

        time.sleep(12)

        assert "/inventory.html" in driver.current_url , "no se dirigio al inventario"
    
        print("prueba exitosa") 
    
    except Exception as e:
        print(f"Error en el login: {e}")
        raise 
    finally:
        driver.quit()    