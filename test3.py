#driver = webdriver.Chrome('/Users/german/Desktop/chromedriver_mac64')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger

logger.add("logging", format="{time}, {level} , {message}", level="DEBUG")


def test3():
    driver = webdriver.Chrome()
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    logger.log(3, 'Enter the site -www.globalsqa.com-')
    driver.fullscreen_window()
    logger.log(3, 'fullscreen')
    time.sleep(2)


    meneger = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
    meneger.click()
    logger.log(3, 'Click on bank manager login')
    time.sleep(2)

    add = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]')
    add.click()
    logger.log(3, 'Click on add customers')
    time.sleep(2)

    last = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input')
    last.click()
    logger.log(3, 'Click on text box last name')
    time.sleep(2)

    lastname = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input')
    lastname.send_keys('Rahanaev')
    logger.log(3, 'enter Rahanaev')
    time.sleep(2)

    code = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input')
    code.click()
    logger.log(3, 'Click on text box post code')
    time.sleep(2)

    code = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input')
    code.send_keys('80100')
    logger.log(3, 'enter 80100')
    time.sleep(2)

    meneger = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
    meneger.click()
    logger.log(3, 'Click on add customers')
    driver.save_screenshot('the test result.png')
    logger.log(3, 'take screenshot')
    time.sleep(2)

    try:
        driver.switch_to.alert.accept()
        print('work as proper ')
    except:
        print('name is empty')
