# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta


class MarketplaceNotification(models.Model):
    _name = 'marketplace.notification'
    _description = 'Marketplace Notifications'
    _order = 'trigger_datetime desc'

    title = fields.Char(string='Title', required=True)
    message = fields.Text(string='Message', required=True)
    notification_type = fields.Selection([
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('error', 'Error'),
    ], string='Type', default='info', required=True)
    user_id = fields.Many2one(
        'res.users',
        string='User to Notify',
        required=True,
        default=lambda self: self.env.user
    )
    state = fields.Selection([
        ('new', 'New'),
        ('sent', 'Sent'),
        ('read', 'Read'),
    ], string='State', default='new', required=True)
    trigger_datetime = fields.Datetime(
        string='Trigger DateTime',
        required=True,
        default=fields.Datetime.now
    )
    related_model = fields.Char(string='Related Model (e.g. sale.order)')
    related_record_id = fields.Integer(string='Related Record ID')
    created_at = fields.Datetime(string='Created At', readonly=True, default=fields.Datetime.now)

    def action_mark_as_read(self):
        """Mark notification as read"""
        self.state = 'read'

    def action_mark_as_sent(self):
        """Mark notification as sent"""
        self.state = 'sent'

    def action_resend(self):
        """Resend notification"""
        self.state = 'new'

    @api.model
    def _generate_sample_notifications(self):
        """Generate sample notifications (for demo/testing)"""
        # This method can be called by cron to generate sample notifications
        # In production, you would implement actual event-based notification logic
        pass
