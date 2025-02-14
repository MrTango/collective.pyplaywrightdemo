# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.pyplaywrightdemo


class CollectivePyplaywrightdemoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.pyplaywrightdemo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.pyplaywrightdemo:default")


COLLECTIVE_PYPLAYWRIGHTDEMO_FIXTURE = CollectivePyplaywrightdemoLayer()


COLLECTIVE_PYPLAYWRIGHTDEMO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PYPLAYWRIGHTDEMO_FIXTURE,),
    name="CollectivePyplaywrightdemoLayer:IntegrationTesting",
)


COLLECTIVE_PYPLAYWRIGHTDEMO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PYPLAYWRIGHTDEMO_FIXTURE,),
    name="CollectivePyplaywrightdemoLayer:FunctionalTesting",
)


COLLECTIVE_PYPLAYWRIGHTDEMO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PYPLAYWRIGHTDEMO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectivePyplaywrightdemoLayer:AcceptanceTesting",
)
