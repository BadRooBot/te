import os
import shutil
import time
import schedule

# from flask import Flask, Request, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import requests
driver_path = "edge_driver/msedgedriver.exe"
base_url='https://d.apkpure.net/b/APK/com.blacklotus.app?versionCode=5';
options = EdgeOptions()
# options.headless = True
# options.add_argument('headless')
service = EdgeService(executable_path=driver_path)
driver = webdriver.Edge(service=service, options=options)
driver.get('https://blacklotusai.blogspot.com/')
filename='_1.0.5_Apkpure.apk'
def good_luck():
    try:
        driver.get(base_url)
        time.sleep(1)
        print("File downloaded successfully.")
    except Exception as e:
        good_luck()
    finally:
        if os.path.exists(filename):
            try:
                print(f"Removing existing file: {filename}")
                os.remove(filename)
            except:    
                            good_luck()
        for  i in range(100):
            if os.path.exists(f"_1.0.5_Apkpure ({i}).apk"):
                try:
                    print(f"Removing incomplete download: {filename}.part")
                    os.remove(f"_1.0.5_Apkpure ({i}).apk")
                except:    
                            good_luck()


        print("Good Luck for Test")

schedule.every(.8).seconds.do(good_luck)

while True:
    schedule.run_pending()
    time.sleep(1)
# class Bot:
#     def __init__(self):
#         # self.driver_path = "edge_driver/msedgedriver.exe"
#         # self.options = EdgeOptions()
#         # self.options.headless = True
#         # # self.options.add_argument('headless')
#         # self.service = EdgeService(executable_path=self.driver_path)
#         # self.driver = webdriver.Edge(service=self.service, options=self.options)
        
#     def start(self, home_page):
#         self.driver.get(home_page)
#         print(f'Bot is started ++++={self.driver.title}')

#     def stop(self):
#         self.driver.quit()

# app = Flask(__name__)
# @app.route('/')
# def home():
#         return redirect('https://d.apkpure.net/b/APK/com.blacklotus.app?versionCode=3', code=301)
# @app.route('/start')
# def start():
#     # bot.start(home_page="https://d.apkpure.net/b/APK/com.blacklotus.app?versionCode=3")
#     while True:
                
#         response = requests.get("http://127.0.0.1:5000/")
#         time.sleep(4)
#         os.remove('_1.0.3_Apkpure.apk');

#     return 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'

# @app.route('/stop')
# def stop():
#     # bot.stop()
#     return 'Bot stopped.'

# if __name__ == '__main__':
#     app.run(debug=False)