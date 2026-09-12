# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MarketplaceCoupon(models.Model):
    _name = 'marketplace.coupon'
    _description = 'Marketplace Coupons'
    _order = 'create_date desc'

    name = fields.Char(string='Coupon Name', required=True)
    code = fields.Char(string='Coupon Code', required=True, index=True)
    coupon_type = fields.Selection([
        ('percentage', 'Percentage Discount'),
        ('fixed', 'Fixed Amount'),
        ('free_shipping', 'Free Shipping'),
    ], string='Type', default='percentage', required=True)
    amount = fields.Float(string='Amount', required=True, default=0.0)
    vendor_id = fields.Many2one('marketplace.vendor', string='Vendor', required=True)
    valid_from = fields.Date(string='Valid From', required=True)
    valid_to = fields.Date(string='Valid To', required=True)
    usage_limit = fields.Integer(string='Usage Limit', default=0, help='0 = unlimited')
    usage_count = fields.Integer(string='Times Used', default=0, readonly=True)
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Notes')
    is_valid = fields.Boolean(string='Is Valid', compute='_compute_is_valid', store=False)

    @api.depends('valid_from', 'valid_to')
    def _compute_is_valid(self):
        """Compute if coupon is within valid date range (PLACEHOLDER)"""
        today = fields.Date.today()
        for record in self:
            if record.valid_from and record.valid_to:
                record.is_valid = (record.valid_from <= today <= record.valid_to)
            else:
                record.is_valid = False

    @api.constrains('valid_from', 'valid_to')
    def _check_dates(self):
        """Ensure valid_from is before valid_to"""
        for record in self:
            if record.valid_from > record.valid_to:
                raise ValueError('Valid From date must be before Valid To date.')

    @api.constrains('amount')
    def _check_amount(self):
        """Ensure amount is positive"""
        for record in self:
            if record.amount < 0:
                raise ValueError('Amount must be positive.')

    def action_increment_usage(self):
        """Increment usage counter (PLACEHOLDER for future integration)"""
        self.usage_count += 1
