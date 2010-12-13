# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import GlobalSectionsViewlet as BaseGlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class GlobalSectionsViewlet(BaseGlobalSectionsViewlet):
    index = ViewPageTemplateFile('sections.pt')

