from playwright.sync_api import Page
import pytest


class Testbugzone_shop:

    def __init__(self, page):
        self.page = page

    def start_wait(self):  # ページの表示待機とショップへ移動
        self.page.goto("file:///C:/Users/takeru.chikuta/Documents/VSVN_bugzone/web/index.html",wait_until = "networkidle")
        self.page.click("body > div.hero-area.hero-bg > div > div > div > div > div > div.hero-btns > a")
        self.page.wait_for_load_state()

    def check_shop(self):  # shop画面確認
        assert self.page.text_content("#sticker > div > div.row > div.col-lg-12.col-sm-12.text-center > div > nav > ul > li:nth-child(1) > a") == "商品一覧 ", "遷移出来ていません"

    def category_click(self, category):  # カテゴリを選択
        self.page.get_by_role("link", name= category, exact = True).click()

    def category_product(self, category, many):  # カテゴリー選んで売られている商品をmany個カートにシュート！！
        product_list = ["#tableProd > div:nth-child(1) > div > div > a > img", "#tableProd > div:nth-child(2) > div > div > a > img", "#tableProd > div:nth-child(3) > div > div > a > img", "#tableProd > div:nth-child(4) > div > div > a > img", "#tableProd > div:nth-child(5) > div > div > a > img", "#tableProd > div:nth-child(6) > div > div > a > img", "#tableProd > div:nth-child(7) > div > div > a > img", "#tableProd > div:nth-child(8) > div > div > a > img", "#tableProd > div:nth-child(9) > div > div > a > img"]
        product_list_stats = ["#tableProd > div:nth-child(1) > div > p > span", "#tableProd > div:nth-child(2) > div > p > span", "#tableProd > div:nth-child(3) > div > p > span", "#tableProd > div:nth-child(4) > div > p > span", "#tableProd > div:nth-child(5) > div > p > span" "#tableProd > div:nth-child(6) > div > p > span", "#tableProd > div:nth-child(7) > div > p > span" ,"#tableProd > div:nth-child(8) > div > p > span", "#tableProd > div:nth-child(9) > div > p > span"]

        stats_ture = 0
        index = 0
        while stats_ture < many:
            self.page.get_by_role("link", name= category, exact = True).click()  # カテゴリークリック
            self.page.wait_for_load_state()
            product_locator = self.page.locator(product_list[index])
            stats_locator = self.page.locator(product_list_stats[index])
            stats_text =stats_locator.inner_text()
            if stats_text == "販売中":
                product_locator.click()  # 商品をクリックして商品詳細に遷移
                self.page.wait_for_load_state()
                self.page.fill("#numItem", "1")  # 数量に1を入力
                self.page.click("#showProd > div.col-md-7 > div > div > a > i")  # カートに入れる
                self.page.wait_for_selector("#toastMe > div > div > div.toast-body")
                self.page.click("#sticker > div > div.row > div > div > nav > ul > li:nth-child(1) > a")  # 商品一覧をクリック
                index = index + 1
                stats_ture = stats_ture + 1
                continue
            elif stats_text == "売り切れ":
                index = index + 1
                continue

    def category_and_product_many(self, category_number, product_many, quantity):  # カテゴリ数、商品の種類、商品の個数を入力
        category_locator = ["#sidermenu > li:nth-child(2) > a", "#sidermenu > li:nth-child(3) > a", "#sidermenu > li:nth-child(4) > a", "#sidermenu > li:nth-child(5) > a", "#sidermenu > li:nth-child(6) > a", "#sidermenu > li:nth-child(7) > a", "#sidermenu > li:nth-child(8) > a", "#sidermenu > li:nth-child(9) > a", "#sidermenu > li:nth-child(10) > a", "#sidermenu > li:nth-child(11) > a" "#sidermenu > li:nth-child(12) > a"]
        # 各カテゴリーのロケータを上から入れている
        product_list = ["#tableProd > div:nth-child(1) > div > div > a > img", "#tableProd > div:nth-child(2) > div > div > a > img", "#tableProd > div:nth-child(3) > div > div > a > img", "#tableProd > div:nth-child(4) > div > div > a > img", "#tableProd > div:nth-child(5) > div > div > a > img", "#tableProd > div:nth-child(6) > div > div > a > img", "#tableProd > div:nth-child(7) > div > div > a > img", "#tableProd > div:nth-child(8) > div > div > a > img", "#tableProd > div:nth-child(9) > div > div > a > img"]
        # 各商品のリンク場所
        category_count = 0
        while category_count < category_number:
            category_locator_in = self.page.locator(category_locator[category_count])
            category_locator_in.click()
            self.page.wait_for_selector("#d1")
            self.page.click("#d1")
            self.page.get_by_role("link", name= '販売中', exact = True).click()  # 販売中のみにするのフィルター設定
            product_many_0 = int(product_many) - 1  # リスト呼びだしのために0を含ませる
            is_product = self.page.is_visible(product_list[product_many_0])
            # そのカテゴリのproduct_many個目の商品があるか確認

            if is_product is True:
                product_count = 0
                while product_count < product_many:  # 商品をカートに入れる繰り返し文
                    product_locator_in = self.page.locator(product_list[product_count])
                    product_locator_in.click()
                    self.page.wait_for_load_state()
                    quantity = str(quantity)
                    self.page.fill("#numItem", quantity)  # 数量に個数を入力
                    self.page.click("#showProd > div.col-md-7 > div > div > a > i")  # カートに入れる
                    self.page.wait_for_selector("#toastMe > div > div > div.toast-body")  # 完了ダイアログ待機
                    self.page.click("#sticker > div > div.row > div > div > nav > ul > li:nth-child(1) > a")  # 商品一覧をクリック
                    self.page.wait_for_load_state()
                    product_count = product_count + 1
                category_count = category_count + 1
                continue
            elif is_product is False:
                category_count = category_count + 1
                continue

            cart_on = self.page.get_by_role("#cartNum").is_visible()  # カートに入っている個数の表記があるか

            if cart_on == True:
                total_product = int(category_number) * int(product_many)
                total_product = str(total_product)
                assert self.page.text_content("#cartNum") == total_product, "販売中の商品が引数productには足りませんでした"  # カートの個数が引数から予測される個数と等しいか
            elif cart_on == False:
                assert cart_on == True, "販売中の商品が引数productには足りませんでした"

    def sold_out_in(self):  # 売り切れ商品を一つカートに入れようとする
        category_locator = ["#sidermenu > li:nth-child(2) > a", "#sidermenu > li:nth-child(3) > a", "#sidermenu > li:nth-child(4) > a", "#sidermenu > li:nth-child(5) > a", "#sidermenu > li:nth-child(6) > a", "#sidermenu > li:nth-child(7) > a", "#sidermenu > li:nth-child(8) > a", "#sidermenu > li:nth-child(9) > a", "#sidermenu > li:nth-child(10) > a", "#sidermenu > li:nth-child(11) > a" "#sidermenu > li:nth-child(12) > a"]
        # 各カテゴリーのロケータを上から入れている

        category_count = 0
        quantity = 0
        while quantity < 1 and category_count < 13:
            category_locator_in = self.page.locator(category_locator[category_count])
            category_locator_in.click()
            self.page.wait_for_selector("#d1")
            self.page.click("#d1")
            self.page.get_by_role("link", name= '売り切れ', exact = True).click()  # 売り切れのみにするのフィルター設定
            is_product = self.page.is_visible("#tableProd > div:nth-child(1) > div > div > a > img")
            # そのカテゴリの1個目の商品があるか確認

            if is_product is True:
                product_count = 0
                self.page.click("#tableProd > div:nth-child(1) > div > div > a > img")
                self.page.wait_for_load_state()
                self.page.fill("#numItem", "1")  # 数量に1を入力
                self.page.click("#showProd > div.col-md-7 > div > div > a > i")  # カートに入れる
                self.page.wait_for_timeout(3000)  # カートに入るかもなので3秒待つ
                self.page.click("#sticker > div > div.row > div > div > nav > ul > li:nth-child(1) > a")  # 商品一覧をクリック
                self.page.wait_for_load_state()
                category_count = category_count + 1
                quantity = quantity + 1
            elif is_product is False:
                category_count = category_count + 1

        assert quantity == 1,"売り切れ商品がありませんでした"

