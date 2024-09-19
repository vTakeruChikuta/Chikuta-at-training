from playwright.sync_api import Page
import pytest
from pages import form


class TestHotelPlanisphere(object):
    @pytest.fixture(scope="function", autouse = True)
    def page_fixture(self, page: Page):
        self.page = page
        yield
        self.page.close()

    def test_change_day_error(self):  # テストケース1「前日指定時のエラー」
        page = self.page
        form_page = form.TestHotel_form(page)

        form_page.stert_wait()  # ページの表示待機
        form_page.set_date_plus_mines(-1)  # 日付の入力を任意の日にちを-1して入力
        form_page.check_date_error()  # 日付の入力ミスで出力されるエラーメッセージの確認

    def test_none_name(self):  # テストケース2「名前未入力エラー」
        page = self.page
        form_page = form.TestHotel_form(page)

        form_page.stert_wait()  # ページの表示待機
        form_page.neme_in("")  # 名前を未入力に
        form_page.enter_submit()  # 予約確定ボタンを押下
        form_page.check_name_error()  # 名前未入力エラーの確認

    def test_after_90day(self):  # テストケース3「日付90日超えエラー」
        page = self.page
        form_page = form.TestHotel_form(page)

        form_page.stert_wait()  # ページの表示待機
        form_page.set_date_plus_mines(91)  # 91日後を設定
        form_page.check_date_error_over()  # 日付の入力が超過したときのエラー確認
