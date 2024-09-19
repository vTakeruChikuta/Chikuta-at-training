import pytest
from playwright.sync_api import Page
from pages_bz import shop,cart

class Testbugzone(object):
    @pytest.fixture(scope="function", autouse =True)
    def page_fixture(self, page: Page):
        self.page = page
        yield
        self.page.close()

    def test_Category_3item(self):  # 違うカテゴリ3つで5%割引
        shop_page = shop.Testbugzone_shop(self.page)
        cart_page = cart.Testbugzone_cart(self.page)

        shop_page.start_wait()
        shop_page.category_and_product_many(3, 1, 1)
        cart_page.assert_five_discount("test_Category_3item.png")

    def test_Category_5item(self):  # 商品を5個で10%引き
        shop_page = shop.Testbugzone_shop(self.page)
        cart_page = cart.Testbugzone_cart(self.page)

        shop_page.start_wait()
        shop_page.category_and_product_many(1, 1, 1)
        cart_page.cart_edit(1, 5)
        cart_page.assert_ten_discount("test_Category_5item.png")

    def test_sold_out_cant_in(self):  # 売り切れ商品をカートに入れられない事を確認
        shop_page = shop.Testbugzone_shop(self.page)
        cart_page = cart.Testbugzone_cart(self.page)

        shop_page.start_wait()
        shop_page.sold_out_in()
        cart_page.assert_non("test_sold_out_cant_in.png")
