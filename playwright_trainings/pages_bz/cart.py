from playwright.sync_api import Page
import pytest


class Testbugzone_cart:

    def __init__(self, page):
        self.page = page

    def assert_five_discount(self, ssname):  # 5%割引の確認
        self.page.click("#sticker > div > div.row > div.col-lg-12.col-sm-12.text-center > div > nav > ul > li:nth-child(3) > div > a")
        self.page.wait_for_timeout(1000)
        self.page.screenshot(path=ssname)

        def number_text(locator):
            import re
            locator = self.page.locator(locator)
            discount = locator.inner_text()
            discount_numbers = re.sub(r"\D", "", discount)  # re関数で正規表現をもとに数字のみ抜き出し
            return discount_numbers


        bill_numbers = number_text("#totalTable > tr:nth-child(1) > td.product-name3.totalAll")
        bill_numbers = int(bill_numbers)

        discount_numbers = number_text("#totalTable > tr:nth-child(2) > td.product-name3.totalVoucher")
        discount_numbers = int(discount_numbers)

        shipping_numbers = number_text("#totalTable > tr:nth-child(2) > td.product-name3.totalVoucher")
        shipping_numbers = int(shipping_numbers)

        total_bill_numbers = number_text("#totalTable > tr:nth-child(4) > td.product-name4.total")
        total_bill_numbers = int(total_bill_numbers)

        assert int(round(bill_numbers * 0.05)) == discount_numbers, "割引金額エラー"
        assert self.page.text_content("#totalTable > tr:nth-child(2) > td.product-name2.waribiki") == "割引 （5％ オフ）", "割引率表記エラー"
        total_bill = bill_numbers - int(round(bill_numbers * 0.05)) + shipping_numbers
        assert total_bill == total_bill_numbers, "合計金額エラー"

    def assert_ten_discount(self, ssname):  # 10%割引の確認
        self.page.click("#sticker > div > div.row > div.col-lg-12.col-sm-12.text-center > div > nav > ul > li:nth-child(3) > div > a")
        self.page.wait_for_timeout(1000)
        self.page.screenshot(path=ssname)

        def number_text(locator):
            import re
            locator = self.page.locator(locator)
            discount = locator.inner_text()
            discount_numbers = re.sub(r"\D", "", discount)  # re関数で正規表現をもとに数字のみ抜き出し
            return discount_numbers


        bill_numbers = number_text("#totalTable > tr:nth-child(1) > td.product-name3.totalAll")
        bill_numbers = int(bill_numbers)

        discount_numbers = number_text("#totalTable > tr:nth-child(2) > td.product-name3.totalVoucher")
        discount_numbers = int(discount_numbers)

        shipping_numbers = number_text("#totalTable > tr:nth-child(2) > td.product-name3.totalVoucher")
        shipping_numbers = int(shipping_numbers)

        total_bill_numbers = number_text("#totalTable > tr:nth-child(4) > td.product-name4.total")
        total_bill_numbers = int(total_bill_numbers)

        assert int(round(bill_numbers * 0.1)) == discount_numbers, "割引金額エラー"
        assert self.page.text_content("#totalTable > tr:nth-child(2) > td.product-name2.waribiki") == "割引 （10％ オフ）", "割引率表記エラー"
        total_bill = bill_numbers - int(round(bill_numbers * 0.1)) + shipping_numbers
        assert total_bill == total_bill_numbers, "合計金額エラー"

    def cart_edit(self, product, quantity,):  # 上からｐ個の商品をｑ個に設定　0で削除
        self.page.click("#sticker > div > div.row > div.col-lg-12.col-sm-12.text-center > div > nav > ul > li:nth-child(3) > div > a")
        self.page.wait_for_load_state()
        quantity_fill_list = ["#id32", "#id351", "#id355", "#id33", "#id343", "#id345", "#id341", "#id352", "#id35"]

        count = 0
        while product > count:
            if quantity > 0:
                self.page.wait_for_timeout(1000)
                quantity = str(quantity)
                self.page.fill(quantity_fill_list[count], quantity)
                count = count + 1
                continue
            elif quantity == 0:
                click("#row-item-id322 > td.product-remove > a > img")
                self.page.wait_for_selector("#delkButton")
                click("#delkButton")
                count = count + 1
                continue

    def assert_non(self, ssname):  # カートに商品が入っていないことを確認する
        self.page.click("#sticker > div > div.row > div.col-lg-12.col-sm-12.text-center > div > nav > ul > li:nth-child(3) > div > a")
        self.page.wait_for_load_state()
        self.page.wait_for_timeout(1000)
        self.page.screenshot(path=ssname)

        assert self.page.text_content("#totalTable > tr:nth-child(1) > td.product-name3.totalAll") == "¥ 0", "カートに商品が入っています"
