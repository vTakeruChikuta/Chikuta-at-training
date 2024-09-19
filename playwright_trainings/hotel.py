import pytest
from playwright.sync_api import Page
from pages_ho import 


class Testbugzone(object):
    @pytest.fixture(scope="function", autouse =True)
    def page_fixture(self, page: Page):
        self.page = page
        yield
        self.page.close()
