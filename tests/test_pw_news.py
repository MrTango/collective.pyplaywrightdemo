import re
import os
import pytest
from playwright.sync_api import Page, expect
from plone.app.testing.interfaces import SITE_OWNER_NAME
from plone.app.testing.interfaces import SITE_OWNER_PASSWORD


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     return {"storage_state": "auth.json"}

@pytest.fixture(scope="session")
def auto_login():
    def login(plone_url, page: Page):
        page.goto(f"{plone_url}")
        page.get_by_role("link", name="Log in").click()
        page.get_by_role("textbox", name="Login Name •").click()
        page.get_by_role("textbox", name="Login Name •").fill(f"{SITE_OWNER_NAME}")
        page.get_by_role("textbox", name="Login Name •").press("Tab")
        page.get_by_role("textbox", name="Password •").fill(f"{SITE_OWNER_PASSWORD}")
        page.get_by_role("button", name="Log in").click()
    return login


class TestPwEvents:
    @pytest.fixture(autouse=True)
    def _init(self, portal, plone_url, page: Page, auto_login):
        self.portal = portal
        self.plone_url = plone_url
        auto_login(plone_url, page)


    def test_news_listing(self, page: Page) -> None:
        # page.pause()
        # page.locator("h1").click()
        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Folder").click()
        page.locator("[name='form.widgets.IDublinCore.title']").click()
        page.locator("[name='form.widgets.IDublinCore.title']").fill("News")
        page.get_by_role("button", name="Save").click()
        expect(page.locator("ol")).to_contain_text("News")

        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Collection").click()
        page.get_by_role("textbox", name="Title •").click()
        page.get_by_role("textbox", name="Title •").fill("News aggregator")
        page.get_by_role("link", name="Select criteria").click()
        page.locator(".select2-option-portal-type").click()
        page.get_by_role("group", name="Default").get_by_role("list").click()
        page.get_by_role("option", name="News item").click()
        page.get_by_role("link", name="No sorting").click()
        page.get_by_role("option", name="Effective date").click()
        page.get_by_role("checkbox").check()
        page.get_by_role("button", name="Save").click()
        expect(page.locator("ol")).to_contain_text("News aggregator")


