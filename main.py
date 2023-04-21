from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

def search_image(s):
    if s.find(".") != -1:
        driver.get(s)
    else:
        driver.get('http://www.google.com/search?q=+' + s+'&safe=images&hl=en&sxsrf=APwXEdeZXyl594MxMTf2q1leOlXs4kYjCQ:1682071583825&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjy-fX53Lr-AhWJq6QKHZ48D5gQ_AUoAnoECAEQBA&biw=1280&bih=569&dpr=1.5')
    time.sleep(5)

def image_click(i):
    image_results = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    first_image = image_results[i]
    first_image.click()
    time.sleep(1)

def download_image(i):
    image_element = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    image_url = image_element[i].get_attribute("src")
    local_file = f"D:\\Git-Hub\\Download-API\\Image #{i+1}.jpg"
    urllib.request.urlretrieve(image_url, local_file)

if __name__ == "__main__":
    s = input("SEARCH: ")
    search_image(s)
    print("Downloading Images of "+s)
    for i in range(5):
        image_click(i)
        download_image(i)
    print("All Images Downloaded !")
