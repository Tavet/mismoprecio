# Scrapy
import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Otros
import os
import sys
import time
import uuid
from logzero import logfile, logger

# Módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../modules")))
import pages_module
from aws_module import get_clothes_data

store_name='patprimo'