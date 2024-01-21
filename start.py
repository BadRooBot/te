from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Bot:
    def __init__(self):
        self.driver_path = "edge_driver/msedgedriver.exe"
        self.options = EdgeOptions()
        self.options.headless = True
        # self.options.add_argument('headless')
        self.service = EdgeService(executable_path=self.driver_path)
        self.driver = webdriver.Edge(service=self.service, options=self.options)
        
    def start(self, home_page):
        self.driver.get(home_page)
        print(f'Bot is started ++++={self.driver.title}')

    def stop(self):
        self.driver.quit()

app = Flask(__name__)
bot = Bot()

def home():
    return 'Hello, World! i ABosherif'
@app.route('/start')
def start():
    bot.start(home_page="https://d.apkpure.net/b/APK/com.blacklotus.app?versionCode=3")
    



    return 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'

@app.route('/stop')
def stop():
    bot.stop()
    return 'Bot stopped.'

if __name__ == '__main__':
    app.run(debug=False)