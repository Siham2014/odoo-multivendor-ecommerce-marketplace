# -*- coding: utf-8 -*-
{
    'name': 'Marketplace Delivery Management',
    'version': '16.0.1.0.0',
    'author': 'ElysiumShop',
    'category': 'Inventory/Delivery',
    'summary': 'Delivery tasks and routes management system',
    'description': """
Complete Delivery Management Module

This module provides:
* Delivery task management with tracking numbers
* Delivery route planning and optimization
* Task status tracking (pending, assigned, in transit, delivered, returned, cancelled)
* Automatic sequence generation for tracking numbers (DLV/XXXXX)
* Multiple views: tree, form, kanban, calendar, pivot, graph
* Independent menu system with no external dependencies
* Admin-only access for safe operation
""",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/delivery_sequence.xml',
        'views/delivery_views.xml',
        'views/delivery_actions.xml',
        'views/delivery_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
