# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.icons.fontawesome.testing import (
    COLLECTIVE_ICONS_FONTAWESOME_INTEGRATION_TESTING  # noqa: E501,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.icons.fontawesome is properly installed."""

    layer = COLLECTIVE_ICONS_FONTAWESOME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.icons.fontawesome is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.icons.fontawesome'))

    def test_browserlayer(self):
        """Test that ICollectiveIconsFontawesomeLayer is registered."""
        from collective.icons.fontawesome.interfaces import (
            ICollectiveIconsFontawesomeLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveIconsFontawesomeLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_ICONS_FONTAWESOME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.icons.fontawesome'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.icons.fontawesome is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.icons.fontawesome'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveIconsFontawesomeLayer is removed."""
        from collective.icons.fontawesome.interfaces import \
            ICollectiveIconsFontawesomeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveIconsFontawesomeLayer,
            utils.registered_layers())
