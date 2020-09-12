import time
from math import floor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveTester:
    def __init__(self, urls):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("lang=ko_KR")
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=options
        )
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url):
        BROWSER_HEIGHT = 1080
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0, 0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight"
            )
            total_sections = floor(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections + 1):
                self.browser.execute_script(
                    f"window.scrollTo(0, {section * BROWSER_HEIGHT})"
                )
                time.sleep(2)
                self.browser.save_screenshot(f"screenshots/{size}x{section}.png")

    def start(self):
        for url in self.urls:
            self.screenshot(url)


tester = ResponsiveTester(["https://allforyoung.com"])
tester.start()
