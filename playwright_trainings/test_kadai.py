from playwright.sync_api import Page
import pytest


class TestHotelPlanisphere(object):
    @pytest.fixture(scope="function", autouse = True)
    def page_fixture(self, page: Page):
        self.page = page

        yield

        self.page.close()

    def test_change_day_error(self):  # テストケース1「前日指定時のエラー」
        page = self.page

        page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0",wait_until = "networkidle")

        from datetime import datetime, timedelta
        d_today = datetime.today()
        d_yestaday = d_today - timedelta(days=1)
        d_yestaday_str = d_yestaday.strftime("20%y/%m/%d")
        page.fill("#date", d_yestaday_str)

        page.click("#plan-desc")  # 日付の入力を確定しないとエラーメッセージでないので別の場所をクリック
        page.screenshot(path="case1.png")
        page.wait_for_selector("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div")
        # 確認項目のエラーメッセージが出るまでウェイト
        assert page.text_content("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div") == "翌日以降の日付を入力してください。", "当日以前の日付を設定することができないこと"
        # 日付エラーメッセージの確認

    def test_none_name(self):  # テストケース2「名前未入力エラー」
        page = self.page

        page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0",wait_until = "networkidle")
        page.fill("#username", "")
        page.click("#submit-button")
        page.wait_for_selector("#reserve-form > div > div.col-lg-6.ml-auto > div:nth-child(8) > div")  # エラーメッセージを待機
        page.screenshot(path="case2.png")
        assert page.text_content("#reserve-form > div > div.col-lg-6.ml-auto > div:nth-child(8) > div") == "このフィールドを入力してください。", "名前未入力エラー"
        # 名前欄が空白エラーメッセージの確認

    def test_after_90day(self):  # テストケース3「日付90日超えエラー」
        page = self.page

        page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0",wait_until = "networkidle")

        from datetime import datetime, timedelta
        d_todey = datetime.today()
        d_90day = d_todey + timedelta(days=91)
        d_90day_str = d_90day.strftime("20%y/%m/%d")
        page.fill("#date", d_90day_str)

        page.click("#plan-desc")  # 入力確定のために別の場所をクリック
        page.wait_for_selector("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div")  # エラーメッセージを待機
        page.screenshot(path="case3.png")
        assert page.text_content("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div") == "3ヶ月以内の日付を入力してください。", "90日を超えてのエラー"
        # 予約日が90日より後のエラーメッセージの確認
