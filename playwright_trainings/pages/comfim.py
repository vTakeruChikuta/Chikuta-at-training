from playwright.sync_api import Page
import pytest


class TestHotel_comfim:
    def __init__(self, page):
        self.page = page

    def check_money(self,case,money):  # 結果画面の合計金額の数字部分のみ
        ss = "{}.png".format(case)
        self.page.screenshot(path=ss)
        total_bill = self.page.text_content("#total-bill")
        total_bill_true = "合計 {}円（税込み）".format(money)
        assert total_bill == total_bill_true, "合計金額が違うか、数字のフォーマットが間違っています"
