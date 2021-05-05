# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.icons.fontawesome


class CollectiveIconsFontawesomeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.icons.fontawesome)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.icons.fontawesome:default')


COLLECTIVE_ICONS_FONTAWESOME_FIXTURE = CollectiveIconsFontawesomeLayer()


COLLECTIVE_ICONS_FONTAWESOME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ICONS_FONTAWESOME_FIXTURE,),
    name='CollectiveIconsFontawesomeLayer:IntegrationTesting',
)


COLLECTIVE_ICONS_FONTAWESOME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ICONS_FONTAWESOME_FIXTURE,),
    name='CollectiveIconsFontawesomeLayer:FunctionalTesting',
)


COLLECTIVE_ICONS_FONTAWESOME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_ICONS_FONTAWESOME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveIconsFontawesomeLayer:AcceptanceTesting',
)
