# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from aps.learningsystems import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IApsLearningsystemsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


