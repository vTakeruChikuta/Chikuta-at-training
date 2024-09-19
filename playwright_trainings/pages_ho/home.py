from playwright.sync_api import Page
import pytest


class hotel_home:

    def __init__(self, page):
        self.page = page

    def start_wait(self):  # ページの表示待機とショップへ移動
        self.page.goto("file:///C:/Users/takeru.chikuta/Documents/VSVN_bugzone/web/index.html",wait_until = "networkidle")
        self.page.click("body > div.hero-area.hero-bg > div > div > div > div > div > div.hero-btns > a")
        self.page.wait_for_load_state()
