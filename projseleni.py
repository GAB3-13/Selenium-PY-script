from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/gaby:/classfiles/chromedriver')


driver.get("https://practicesoftwaretesting.com/#/auth/login")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)

driver.find_element(By.ID, "email").send_keys("gabriel@gmail.com")
driver.find_element(By.ID, "password").send_keys("ga@1010AA")
driver.find_element(By.CLASS_NAME, "btnSubmit").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "form-control.ng-pristine.ng-invalid.ng-touched"))
)

search_field = driver.find_element(By.CLASS_NAME, "form-control.ng-pristine.ng-invalid.ng-touched")
search_field.send_keys("hammer")
driver.find_element(By.CLASS_NAME, "btn.btn-secondary").click()



driver.close() 

