import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
from selenium import webdriver
import time 

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # Проскроллить страницу вниз
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    
    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла