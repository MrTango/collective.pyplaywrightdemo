import pytest
from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
from plone.restapi.testing import RelativeSession
from pytest_plone import fixtures_factory
from pythongettext.msgfmt import Msgfmt
from pythongettext.msgfmt import PoSyntaxError
from typing import Generator
from pathlib import Path
from plone.testing.zope import WSGI_SERVER_FIXTURE
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
def portal(acceptance):
    portal = acceptance["portal"]
    # with transaction.manager:
        # contents = create_content_tree()
    yield portal
    # with transaction.manager:
    #     for uid in contents[::-1]:
    #         obj = api.content.get(UID=uid)
    #         if obj:
    #             api.content.delete(obj)


@pytest.fixture()
def request_factory(portal):
    def factory():
        url = portal.absolute_url()
        api_session = RelativeSession(url)
        api_session.headers.update({"Accept": "application/json"})
        return api_session

    return factory


@pytest.fixture()
def manager_request(request_factory):
    request = request_factory()
    request.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
    yield request
    request.auth = ()
