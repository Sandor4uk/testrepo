from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    #finding first num
    num_first = browser.find_element(By.ID,"num1").text
    num_second = browser.find_element(By.ID,"num2").text
    answer = str(int(num_first)+int(num_second))
    #answer = str(answer)
    print(answer)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{answer}")
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()


    

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()