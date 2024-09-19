from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.python.org")
    page.wait_for_load_state()
    assert "Python" in page.title()
    page.fill("#id-search-field", "pycon")
    page.wait_for_timeout(1000)
    page.click("#submit")
    assert "No results found." not in page.content()
    page.wait_for_timeout(3000)