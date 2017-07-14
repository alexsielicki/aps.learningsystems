# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import aps.learningsystems


class ApsLearningsystemsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=aps.learningsystems)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'aps.learningsystems:default')


APS_LEARNINGSYSTEMS_FIXTURE = ApsLearningsystemsLayer()


APS_LEARNINGSYSTEMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(APS_LEARNINGSYSTEMS_FIXTURE,),
    name='ApsLearningsystemsLayer:IntegrationTesting'
)


APS_LEARNINGSYSTEMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(APS_LEARNINGSYSTEMS_FIXTURE,),
    name='ApsLearningsystemsLayer:FunctionalTesting'
)


APS_LEARNINGSYSTEMS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        APS_LEARNINGSYSTEMS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ApsLearningsystemsLayer:AcceptanceTesting'
)
