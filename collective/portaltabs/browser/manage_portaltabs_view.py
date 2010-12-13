# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from collective.portaltabs import portaltabsMessageFactory

class ManagePortaltabsView(BrowserView):
    
    template = ViewPageTemplateFile('manage_portaltabs.pt')
    DEFAULTS = ('portal_tabs|Portal tabs',)
    
    def _prettify(self, url_expr):
        if not url_expr.startswith('python:') and not url_expr.startswith('string:'):
            return 'tal:' + url_expr
        if url_expr.startswith('string:'):
            return url_expr[7:]
        return url_expr
        
    def _simplify(self, action):
        tabs = []
        for x in action.items():
            t = x[1]
            tabs.append({'id': t.id,
                         'title': t.title,
                         'url': self._prettify(t.getProperty('url_expr','')),
                         })
        return tabs
    
    def actions(self):
        """Return current saved tabs"""
        portal_actions = getToolByName(self.context, 'portal_actions')
        results = []
        for x in self.DEFAULTS:
            if x.find("|")>-1:
                id, title = x.split("|")
            else:
                id = title = x
            results.append({'id': id, 'title': title, 'tabs': self._simplify(portal_actions[id])})
        return results
    
    def update(self, form):
        """Update existings"""
        portal_actions = getToolByName(self.context, 'portal_actions')
        actions = form.get('action', [])
        ids = form.get('id', [])
        titles = form.get('title', [])
        urls = form.get('url', [])
    
    def __call__(self):
        self.request.set('disable_border', True)
        if self.request.get('Save'):
            self.update(self.request.form)
        elif self.request.get('Add'):
            self.addNew()
        return self.template()

