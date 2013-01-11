# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName

from collective.portaltabs import logger

PROFILE_ID = 'profile-collective.portaltabs:default'

def _cleanPropertySheet(context):
    # phase 1: copy properties to registry
    # phase 2: delete property sheet
    pass 

def migrateTo2010(context):
    setup_tool = getToolByName(context, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(PROFILE_ID)
    _cleanPropertySheet(context)
    logger.info("Migrated to 0.3.0")
