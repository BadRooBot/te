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
import requests

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

if __name__ == '__main__':
    app.run(debug=False)