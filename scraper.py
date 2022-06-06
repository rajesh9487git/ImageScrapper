import os
import time
import requests
from selenium import webdriver
import urllib

from selenium.webdriver.common.by import By
searchString= 'croc'
path = r'D:\Ineuron\IneuronProjects\PythonProjects\ImageScrapper\chromedriver.exe'
url = "https://www.google.com/search?q=" + searchString +"&sxsrf=ALiCzsbuEH7CdInQTAv0zcxzyk4ZOuAnRQ:1654183278264&source=lnms&tbm=isch&sa=X&ved=2ahUKEwje1sb1iI_4AhVt4TgGHY_lDh8Q_AUoAXoECAIQAw&biw=1536&bih=754&dpr=1.25"



targetFolder= searchString
imageCount=20

def main():
    if not os.path.exists(targetFolder):
        os.mkdir(targetFolder)
        downloadImages()
    else:
        print("The item you are searching is already downloaded")

def downloadImages():
    driver = webdriver.Chrome(path)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    element= driver.find_element(By.ID, "islmp")
    sub= element.find_elements(by=By.TAG_NAME, value="img")

    for j,i in enumerate(sub):
        if j< imageCount:
            src= i.get_attribute('src')
            try:
                if src!= None:
                    src=str(src)
                    print(src)

                    urllib.request.urlretrieve(src, os.path.join(targetFolder,searchString+str(j)+'.jpg' ))
                else:
                    raise TypeError
            except Exception as e:
                print("fail", e)

    driver.close()

if __name__=="__main__":
    main()













