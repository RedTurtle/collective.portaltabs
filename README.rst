.. contents:: **Table of contents**

Introduction
============

Add to Plone a way to manage site **portal tabs** using the Plone interface and hiding common
syntax difficulties you can find in ZMI.

When you need this
------------------

You need this product when you want to give to your non-technical users the ability to
manage the *portal tabs* section of your Plone site.

Going deeply:

* you don't want (or you can't) that your power user will need to go to ZMI
  (for example, the Plone 4.1 "*Site Administrator*" role can't)
* you still want to make them able to manage portal tabs
* you users don't know nothing about TAL and python, and commonly want only to add static
  links to the site
* your additional tab don't need advanced features like condition for being seen, or permissions
  (for this, you can still go to ZMI)

When you don't need this
------------------------

If you only need to port into Plone interface the "*portal_action*" tool customization, you will find
a great product in `quintagroup.plonetabs`__

__ http://pypi.python.org/pypi/quintagroup.plonetabs/

How to use
==========

First note
----------

This product only manage portal tabs that are not automatically generated from Plone. For this
reason, a warning message is displayed if the "*Automatically generate tabs*" option is selected
in the "*Navigation settings*" panel.

Handling tabs
-------------

From the "*Site Setup*" panel, go to the new "*Manage portal tabs*" link you'll find after the
product installation.

.. image:: http://keul.it/images/plone/collective.portaltabs-0.1.0a-1.png
   :alt: View of the Site Setup panel

The "*Portal Tabs settings*" view is composed by two section; the first one for make changes to
existing tabs (and also order and delete them), and the second for adding new tabs.

.. image:: http://keul.it/images/plone/collective.portaltabs-0.2.0-01.png
   :alt: Manage portal tabs panel view

Newly created tab only need two kind of information: the name of the tab to be displayed (title)
and the URL. When creating a tab you can also handle the id of the tab, or this will be
automatically generated.

What I can write inside an URL section?
---------------------------------------

The product try to hide some of the too-technical feature you have available in the ZMI
portal_actions tool management, however all features are still there.

* to create an absolute link to something, just type the link (e.g: "http://foo.org")
* TAL espression are still available, but you need to start them with a "*tal:*"
* Python expression are still available, but you need to start them with a "*python:*"
* when you need to create links to URL inside the site, just type "*/folder/foo*"
  (note that this path *can* be a content path, but no check are done at all)
* inside an URL, you can still use expressions in the normal form "${foo1/foo2/...}"

Manage additional actions categories
------------------------------------

You can use collective.portaltabs to handle also other categories than "*portal_tabs*". To do this you
need to go to ZMI, in the "*portal_properties*" tool and change the "*portaltabs_settings*".

In the "*manageable_categories*" you can add additional entries::

    portal_tabs|Portal tabs
    foo_tabs|My special tabs 

All entries are if the form "actions_id|Title to be displayed" and the *action_id*
action category *must* be exists.
Going back to the "*Portal Tabs settings*" make possible to handle also those new actions

.. image:: http://keul.it/images/plone/collective.portaltabs-0.2.0-02.png
   :alt: Multiple CMF Category panel

Upload directly an "actions.xml" file
=====================================

If you have defined your own portal tabs using a *Generic Setup* profile, you can upload your ``actions.xml``
(or compatible file) file directly in the manage form.

Plone is an helephant, remember all
-----------------------------------

Please, remember that if you used an ``actions.xml`` in one of your product, Plone will remember all action you have
loaded, and changes done manually later will be reverted if you reinstall the product.

To make Plone stopping remember about those actions, you need to:

* uninstall your product that added the actions
* remove the products from the ``portal_quickinstaller`` ("Contents" tab)
* remove the ``actions.xml`` file from your product
* install again

TODO
====

* Block users from creating TAL/Python expressions if you don't want
* Tests

Bug report and feature request
==============================

Please, go to the `product's issue tracker`__ on plone.org website.

__ http://plone.org/products/collective.portaltabs/issues/

Credits
=======

Developed with the support of:

* `S. Anna Hospital, Ferrara`__
  
  .. image:: http://www.ospfe.it/ospfe-logo.jpg 
     :alt: S. Anna Hospital logo

* `Azienda USL Ferrara`__

  .. image:: http://www.ausl.fe.it/logo_ausl.gif
     :alt: Azienda USL logo

All of them supports the `PloneGov initiative`__.

__ http://www.ospfe.it/
__ http://www.ausl.fe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/
