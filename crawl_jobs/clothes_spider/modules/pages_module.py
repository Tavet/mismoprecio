import os
import time


def get_driver_path():
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../_static/drivers/chromedriver.exe"))

def infinite_scroll(driver, timeout):
    scroll_pause_time = timeout
    last_height = driver.execute_script(
        "return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script(
            "return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
