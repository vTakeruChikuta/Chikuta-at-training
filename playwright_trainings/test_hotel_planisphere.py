from playwright.sync_api import Page
import pytest


class TestHotelPlanisphere(object):
    @pytest.fixture(scope="function", autouse = True)
    def page_fixture(self, page: Page):
        self.page = page
        yield
        self.page.close()  # ページを開いてから閉じるまで

    def test_change_all_params(self):

        page = self.page

        page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0",wait_until = "networkidle")

        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        d_today = datetime.today()
        d_today = d_today + relativedelta(months=1)
        d_today_str = d_today.strftime("20%y/%m/01")
        page.fill("#date", d_today_str)
        page.fill("#term", '3')
        page.fill("#head-count", '2')
        page.check('#sightseeing')
        page.fill("#username", '高塩')
        page.select_option('#contact', label="希望しない")
        page.click("#submit-button")
        page.wait_for_load_state()
        page.screenshot(path="sample.png")
        assert page.text_content("#total-bill") == "合計 44,000円（税込み）"
