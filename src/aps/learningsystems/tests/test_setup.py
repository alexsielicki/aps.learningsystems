# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from aps.learningsystems.testing import APS_LEARNINGSYSTEMS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that aps.learningsystems is properly installed."""

    layer = APS_LEARNINGSYSTEMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if aps.learningsystems is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'aps.learningsystems'))

    def test_browserlayer(self):
        """Test that IApsLearningsystemsLayer is registered."""
        from aps.learningsystems.interfaces import (
            IApsLearningsystemsLayer)
        from plone.browserlayer import utils
        self.assertIn(IApsLearningsystemsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = APS_LEARNINGSYSTEMS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['aps.learningsystems'])

    def test_product_uninstalled(self):
        """Test if aps.learningsystems is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'aps.learningsystems'))

    def test_browserlayer_removed(self):
        """Test that IApsLearningsystemsLayer is removed."""
        from aps.learningsystems.interfaces import IApsLearningsystemsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IApsLearningsystemsLayer, utils.registered_layers())
