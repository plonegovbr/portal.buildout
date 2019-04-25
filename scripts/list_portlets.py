# -*- coding: utf-8 -*-
"""
This script list portlet assigments on a site.

Run the script using the following command line:

.. code-block:: console

    $ bin/instance -O Plone run scripts/list_portlets.py

The -O parameter is used to specify the id of your Plone site.

"""
from __future__ import print_function
from plone import api
from plone.portlets.interfaces import ILocalPortletAssignable
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from zope.component import getMultiAdapter
from zope.component import getUtility


def get_valid_objects():
    """Generate a list of objects associated with valid brains."""
    catalog = api.portal.get_tool('portal_catalog')
    results = catalog()
    print('Found {0} objects in the catalog'.format(len(results)))
    for b in api.content.find():
        try:
            obj = b.getObject()
        except (AttributeError, KeyError):
            obj = None

        if obj is None:  # warn on broken entries in the catalog
            msg = 'Invalid object reference in the catalog: {0}'
            print(msg.format(b.getPath()))
            continue

        yield obj


def list_portlet_assignments(obj):
    """List all portlet assignments on a given object."""
    if not ILocalPortletAssignable.providedBy(obj):
        return

    print('object: {0}'.format(obj))
    for name in ('plone.leftcolumn', 'plone.rightcolumn'):
        manager = getUtility(IPortletManager, name=name)
        mapping = getMultiAdapter((obj, manager), IPortletAssignmentMapping)
        items = list(mapping.items())
        if not items:
            continue

        print('├─ {0}'.format(name))
        for k, v in items:
            print('├─── {0} ({1})'.format(k, v))


# list portlets assigned to catalogued objects
for obj in get_valid_objects():
    list_portlet_assignments(obj)

# list portlets assigned to portal root
list_portlet_assignments(api.portal.get())
