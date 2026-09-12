# -*- coding: utf-8 -*-
{
    'name': 'Marketplace Notifications',
    'version': '16.0.1.0.0',
    'author': 'ElysiumShop',
    'category': 'Marketplace/Notifications',
    'summary': 'Internal notification system for marketplace events',
    'description': """
Marketplace Notifications Module

This module provides:
* Internal notification system (marketplace.notification)
* Notification states: new, sent, read
* Multiple notification types: info, warning, error
* Advanced views: tree, form, kanban, pivot, graph, search
* User-specific notifications
* Automatic notification scheduling (cron jobs)
* Related record tracking (model + record_id)
* Independent notification menu in sidebar
* Admin-only access for safe operation
""",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/notification_cron.xml',
        'views/notification_views.xml',
        'views/notification_actions.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
