# -*- coding: utf-8 -*-
{
    'name': 'Marketplace Coupons & Dynamic Pricing',
    'version': '16.0.1.0.0',
    'author': 'ElysiumShop',
    'category': 'Sales/Marketplace',
    'summary': 'Vendor coupons and dynamic pricing engine',
    'description': """
Complete Marketplace Coupons & Dynamic Pricing Module

This module provides:
* Vendor coupon management (percentage, fixed, free shipping)
* Coupon usage tracking and limits
* Dynamic pricing strategy engine
* Pricing margin rules (min/max)
* Security groups for coupon and pricing management
* Advanced views: tree, form, kanban, pivot, graph, search
* Coupon sequences: COUPON/YYYY/00001
""",
    'depends': [
        'base',
        'marketplace_vendor',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/coupon_views.xml',
        'views/dynamic_pricing_views.xml',
        'views/coupon_actions.xml',
        'views/coupon_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
