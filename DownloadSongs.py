from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#URL TO FIRST SONG IN PLAYLIST
url = "https://www.youtube.com/watch?v=h--P8HzYZ74&list=PLLniz7eUcOG1vERNmYm8ApEXSiZfw_BGk&index=1"
ymp = "https://ytmp3.cc/"
switchDelay = 1
waitoutDelay = 30
songcount = 1
#LOCATION OF CHROMEDRIVER
driveLocation = "C:\\Users\\austi\\Desktop\\github\\chromedriver.exe"

driver = webdriver.Chrome(driveLocation)
driver.execute_script("window.open('http://google.com', 'new_window')")
driver.get(url)
driver.switch_to_window(driver.window_handles[1])
driver.get(ymp)
driver.switch_to_window(driver.window_handles[0])

while(1):
    holdurl = driver.current_url
    driver.switch_to_window(driver.window_handles[1])
    enterElement = WebDriverWait(driver, waitoutDelay).until(
        EC.visibility_of_element_located((By.ID, 'input')))
    enterElement.send_keys(holdurl)
    enterElement.send_keys(u'\ue006')
    downloadElement = WebDriverWait(driver, waitoutDelay).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="file"]')))
    downloadElement.click()
    if len(driver.window_handles) > 2:
        driver.switch_to_window(driver.window_handles[2])
        driver.close()
        driver.switch_to_window(driver.window_handles[1])
    nextElement = WebDriverWait(driver, waitoutDelay).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="download"]/a[2]')))
    nextElement.click()
    driver.switch_to_window(driver.window_handles[0])
    # nextVideo = WebDriverWait(driver, waitoutDelay).until(EC.visibility_of_element_located(
    #     (By.XPATH, '//*[@data-index=' + '\"' + str(songcount) + '\"' + ']')))
    nextVideo = WebDriverWait(driver, waitoutDelay).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="items"]/ytd-playlist-panel-video-renderer[' + str(songcount) + ']')))
    nextVideo.click()
    songcount = songcount + 1
    time.sleep(switchDelay)
