from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#URL TO FIRST SONG IN PLAYLIST
url = "https://www.youtube.com/watch?v=vlCwheTryPU&list=OLAK5uy_ni2Xd4MdhDbtdxFZzIVXg8VckJBsSJLW4&ab_channel=SaidtheSky-Topic"
ymp = "https://ytmp3.cc/"
switchDelay = 1
waitoutDelay = 300
songcount = 1
#LOCATION OF CHROMEDRIVER
driveLocation = "./chromedriver.exe"

driver = webdriver.Chrome(driveLocation)
driver.execute_script("window.open('http://google.com', 'new_window')")
driver.get(url)
driver.switch_to_window(driver.window_handles[1])
driver.get(ymp)
driver.switch_to_window(driver.window_handles[0])
print("starting main loop")
while(1):
    holdurl = driver.current_url
    print(holdurl)
    driver.switch_to_window(driver.window_handles[1])
    enterElement = WebDriverWait(driver, waitoutDelay).until(
        EC.visibility_of_element_located((By.ID, 'input')))
    enterElement.send_keys(holdurl)
    enterElement.send_keys(u'\ue006')
    print("beforeDownload")
    downloadElement = WebDriverWait(driver, waitoutDelay).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="buttons"]/a[1]')))
    print("hit download")
    downloadElement.click()
    if len(driver.window_handles) > 2:
        driver.switch_to_window(driver.window_handles[2])
        driver.close()
        driver.switch_to_window(driver.window_handles[1])
    nextElement = WebDriverWait(driver, waitoutDelay).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="buttons"]/a[3]')))
    nextElement.click()
    driver.switch_to_window(driver.window_handles[0])
    # nextVideo = WebDriverWait(driver, waitoutDelay).until(EC.visibility_of_element_located(
    #     (By.XPATH, '//*[@data-index=' + '\"' + str(songcount) + '\"' + ']')))
    #nextVideo = WebDriverWait(driver, waitoutDelay).until(EC.visibility_of_element_located(
    #    (By.XPATH, '//*[@id="items"]/ytd-playlist-panel-video-renderer[' + str(songcount) + ']')))
    nextVideo = WebDriverWait(driver, waitoutDelay).until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/ytd-playlist-panel-renderer/div/div[2]/ytd-playlist-panel-video-renderer[' + str(songcount) + ']/a')))
    # //*[@id="playlist-items/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/ytd-playlist-panel-renderer/div/div[2]/ytd-playlist-panel-video-renderer[1]
    nextVideo.click()
    songcount = songcount + 1
    time.sleep(switchDelay)
