from selenium import webdriver
from selenium.webdriver.chrome.service import Service

webdriver.Chrome(service=Service('C:/WebDriver/bin/yandexdriver-25.4.0.1973-win64/yandexdriver.exe'))