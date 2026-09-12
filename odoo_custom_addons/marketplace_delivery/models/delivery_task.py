# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class MarketplaceDeliveryTask(models.Model):
    _name = 'marketplace.delivery.task'
    _description = 'Delivery Task'
    _order = 'create_date desc'

    name = fields.Char(string='Task Name', required=True)
    tracking_number = fields.Char(
        string='Tracking Number',
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('marketplace.delivery.task')
    )
    delivery_person = fields.Many2one(
        'res.partner',
        string='Delivery Person',
        required=True,
        domain=[('is_company', '=', False)]
    )
    customer = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        domain=[('is_company', '=', False)]
    )
    address_pickup = fields.Char(string='Pickup Address', required=True)
    address_dropoff = fields.Char(string='Dropoff Address', required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='pending', required=True)
    priority = fields.Integer(string='Priority', default=0)
    expected_date = fields.Date(string='Expected Delivery Date', required=True)
    done_date = fields.Date(string='Actual Delivery Date')
    notes = fields.Text(string='Notes')
    route_id = fields.Many2one('marketplace.delivery.route', string='Delivery Route')

    @api.constrains('expected_date', 'done_date')
    def _check_dates(self):
        for record in self:
            if record.done_date and record.expected_date > record.done_date:
                raise ValueError('Expected date cannot be after actual delivery date.')

    def action_mark_in_transit(self):
        self.status = 'in_transit'

    def action_mark_delivered(self):
        self.status = 'delivered'
        self.done_date = fields.Date.today()

    def action_cancel(self):
        self.status = 'cancelled'
