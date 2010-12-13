# -*- coding: utf-8 -*-

from Products.CMFPlone.browser.navigation import CatalogNavigationTabs as BaseCatalogNavigationTabs

class CatalogNavigationTabs(BaseCatalogNavigationTabs):

    def topLevelTabs(self, actions=None, category='portal_tabs'):
        rawresults = BaseCatalogNavigationTabs.topLevelTabs(self, actions=actions, category=category)
        results = []
        for x in rawresults:
            if x.get('category')=='portal_tabs':
                results.append(x)
            else:
                results.append(x)
        return results

