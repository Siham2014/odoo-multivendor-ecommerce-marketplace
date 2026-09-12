# -*- coding: utf-8 -*-
{
    'name': 'Marketplace Vendor Portal',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'summary': 'Vendor Portal for ElysiumShop Marketplace - Dashboard, Products, Orders, Delivery, SAV, Notifications',
    'description': '''Marketplace Vendor Portal

This module provides a modern vendor portal interface for the ElysiumShop marketplace.

**Features:**

- Vendor Dashboard with statistics
- Product Management
- Order Management and Tracking
- Delivery Status Monitoring
- SAV (Support) Ticket Management
- Notification Center
- Responsive Design with ElysiumShop Colors

**Access:**

- Users with 'Vendor Portal User' group can access the portal via /vendor/portal

**Routes:**

- /vendor/portal - Main dashboard
- /vendor/products - Product management
- /vendor/add-product - Add new product
- /vendor/orders - Order list
- /vendor/delivery - Delivery tracking
- /vendor/sav - SAV tickets
- /vendor/notifications - Notifications

**Security:**

- Portal access restricted to authenticated users
- Group-based access control
- Partner-based data isolation
''',
    'author': 'ElysiumShop',
    'website': 'https://www.elysiumshop.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'website',
        'sale',
        'product',
        'marketplace_delivery',
        'marketplace_sav',
        'marketplace_notifications',
    ],
    'data': [
        'views/portal_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'marketplace_vendor_portal/static/src/css/portal.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
