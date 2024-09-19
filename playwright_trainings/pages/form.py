import pytest
from playwright.sync_api import Page


class TestHotel_form:

    def __init__(self, page):
        self.page = page

    def stert_wait(self):  # ページの表示待機
        self.page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0",wait_until = "networkidle")

    def set_term_headcount(self, team, many):  # 泊数、人数を入力
        self.page.fill("#term", team)
        self.page.fill("#head-count", many)

    def set_date_plus_mines(self, x_days):  # 日付の入力を任意の日にちを+or-して入力
        from datetime import datetime, timedelta
        d_today = datetime.today()
        x_days = int(x_days)
        d_x_day = d_today + timedelta(days= + x_days)
        d_x_day_str = d_x_day.strftime("20%y/%m/%d")
        self.page.fill("#date", d_x_day_str)
        self.page.click("#plan-desc")  # 日付の入力を確定しないとエラーメッセージでないので別の場所をクリック

    def set_plan(self, biking, pm, seeing):  # 追加プランの設定
        if biking == "yes":
            self.page.check("#breakfast")
        if pm == "yes":
            self.page.check("#early-check-in")
        if seeing == "yes":
            self.page.check("#sightseeing")

    def check_date_error(self):  # 日付の入力ミスで出力されるエラーメッセージの確認
        self.page.wait_for_selector("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div")
        # 確認項目のエラーメッセージが出るまでウェイト
        self.page.screenshot(path="date_error.png")
        assert self.page.text_content("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div") == "翌日以降の日付を入力してください。", "当日以前の日付を設定することができないこと"
        # 日付エラーメッセージの確認

    def check_date_error_over(self):  # 日付の入力が超過したときのエラー確認
        self.page.wait_for_selector("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div")  # エラーメッセージを待機
        self.page.screenshot(path="date_over_error.png")
        assert self.page.text_content("#reserve-form > div > div.col-lg-6.ml-auto > div.form-group.was-validated > div") == "3ヶ月以内の日付を入力してください。", "90日を超えてのエラー"
        # 予約日が90日より後のエラーメッセージの確認

    def neme_in(self,name):  # 名前の入力
        self.page.fill("#username", name)

    def enter_submit(self):  # 確定ボタン押下
        self.page.click("#submit-button")

    def check_name_error(self):
        self.page.wait_for_selector("#reserve-form > div > div.col-lg-6.ml-auto > div:nth-child(8) > div")  # エラーメッセージを待機
        self.page.screenshot(path="name_error.png")
        assert self.page.text_content("#reserve-form > div > div.col-lg-6.ml-auto > div:nth-child(8) > div") == "このフィールドを入力してください。", "名前未入力エラー"
        # 名前欄が空白エラーメッセージの確認

    def contact_select(self,contact):  # 確認の連絡プルダウン
        if contact == "no":
            self.page.select_option('#contact', label="希望しない")
        elif contact == "mail":
            self.page.select_option('#contact', label="メールでのご連絡")
            self.page.fill("#email", "takasio@kinniku.com")
        elif contact == "call":
            self.page.select_option('#contact', label="電話でのご連絡")
            self.page.fill("#tel", "08080808080")
