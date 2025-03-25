import base64
from pathlib import Path
from typing import Generator

import pytest
import transaction
from playwright.sync_api import Page
from plone import api
from plone.app.testing.interfaces import (
    SITE_OWNER_NAME,
    SITE_OWNER_PASSWORD,
    TEST_USER_NAME,
)
from plone.testing.zope import WSGI_SERVER_FIXTURE
from pytest_plone import fixtures_factory
from pythongettext.msgfmt import Msgfmt, PoSyntaxError
from zope.component.hooks import setSite

from collective.pyplaywrightdemo.testing import (
    COLLECTIVE_PYPLAYWRIGHTDEMO_ACCEPTANCE_TESTING,
    COLLECTIVE_PYPLAYWRIGHTDEMO_FUNCTIONAL_TESTING,
    COLLECTIVE_PYPLAYWRIGHTDEMO_INTEGRATION_TESTING,
)

pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (COLLECTIVE_PYPLAYWRIGHTDEMO_ACCEPTANCE_TESTING, "acceptance"),
            (COLLECTIVE_PYPLAYWRIGHTDEMO_FUNCTIONAL_TESTING, "functional"),
            (COLLECTIVE_PYPLAYWRIGHTDEMO_INTEGRATION_TESTING, "integration"),
        )
    )
)


def generate_basic_authentication_header_value(username: str, password: str) -> str:
    token = base64.b64encode("{}:{}".format(username, password).encode("utf-8")).decode(
        "ascii"
    )
    return "Basic {}".format(token)


@pytest.fixture(scope="session", autouse=True)
def generate_mo():
    """Generate .mo files."""
    import collective.pyplaywrightdemo

    locales_path = Path(collective.pyplaywrightdemo.__file__).parent / "locales"
    po_files: Generator = locales_path.glob("**/*.po")
    for po_file in po_files:
        parent: Path = po_file.parent
        domain: str = po_file.name[: -len(po_file.suffix)]
        mo_file: Path = parent / f"{domain}.mo"
        try:
            mo = Msgfmt(f"{po_file}", name=domain).getAsFile()
        except PoSyntaxError:
            continue
        else:
            with open(mo_file, "wb") as f_out:
                f_out.write(mo.read())


@pytest.fixture()
def plone_url():
    """"""
    ZOPE_HOST = WSGI_SERVER_FIXTURE.host
    ZOPE_PORT = WSGI_SERVER_FIXTURE.port
    ZOPE_URL = f"http://{ZOPE_HOST}:{ZOPE_PORT}"
    PLONE_SITE_ID = "plone"
    PLONE_URL = f"{ZOPE_URL}/{PLONE_SITE_ID}"
    return PLONE_URL


@pytest.fixture()
def portal_factory(acceptance ,request):
    def factory(roles: list, username: str = TEST_USER_NAME):
        if not roles:
            roles = ['Member']
        portal = acceptance["portal"]
        setSite(portal)
        with api.env.adopt_roles(["Manager", "Member"]):
            api.user.grant_roles(
                username=username,
                roles=roles,
            )
        transaction.commit()

        def cleanup():
            with api.env.adopt_roles(["Manager", "Member"]):
                api.user.revoke_roles(
                    username=username,
                    roles=roles,
                )
            transaction.commit()

        request.addfinalizer(cleanup)
        return portal

    return factory


@pytest.fixture()
def page_factory(new_context):
    def factory(
        username: str = SITE_OWNER_NAME, password: str = SITE_OWNER_PASSWORD
    ) -> Page:
        context = new_context(
            extra_http_headers={
                "Authorization": generate_basic_authentication_header_value(
                    username, password
                ),
            }
        )
        page = context.new_page()
        return page
    return factory
