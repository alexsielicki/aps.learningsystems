from Acquisition import aq_inner
from plone import api
from Products.Five import BrowserView
from plone.dexterity.browser.view import DefaultView
from plone.app.contenttypes.browser.folder import FolderView


class LessonPlanView(DefaultView, FolderView):
	pass
    