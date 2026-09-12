# -*- coding: utf-8 -*-
{
    'name': 'Marketplace Vendor Management',
    'version': '16.0.1.0.0',
    'author': 'ElysiumShop',
    'category': 'Sales/Marketplace',
    'summary': 'Marketplace vendor management, products, and payouts',
    'description': """Complete Marketplace Vendor Management Module

This module provides a complete, independent vendor management system for marketplace operations.

Features:
* Vendor profiles with delegated inheritance from res.partner
* Vendor product listings with pricing
* Vendor payout workflow management
* Security groups: Vendor User and Vendor Manager
* Advanced views: Tree, Form, Kanban, Search
* Payout sequences: PAYOUT/YYYY/00001
* Commission rate tracking
* Status management (active, suspended, banned)
""",
    'depends': [
        'base',
        'sale',
        'product',
        'mail'
    ],
    'data': [
        'views/vendor_views.xml',
        'views/vendor_product_views.xml',
        'views/vendor_payout_views.xml',
        'views/vendor_menu.xml',
        'views/vendor_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
