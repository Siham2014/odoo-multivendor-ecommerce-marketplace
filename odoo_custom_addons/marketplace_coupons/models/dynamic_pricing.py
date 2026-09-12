# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MarketplaceDynamicPricing(models.Model):
    _name = 'marketplace.dynamic.pricing'
    _description = 'Dynamic Pricing Rules'
    _order = 'create_date desc'

    vendor_id = fields.Many2one('marketplace.vendor', string='Vendor', required=True)
    strategy = fields.Selection([
        ('cost_plus', 'Cost Plus'),
        ('demand_based', 'Demand Based'),
        ('manual_override', 'Manual Override'),
    ], string='Pricing Strategy', default='cost_plus', required=True)
    min_margin_percent = fields.Float(string='Minimum Margin %', default=10.0)
    max_margin_percent = fields.Float(string='Maximum Margin %', default=50.0)
    active = fields.Boolean(string='Active', default=True)
    recommended_price = fields.Float(string='Recommended Price', compute='_compute_recommended_price', store=False)

    @api.depends('strategy', 'min_margin_percent', 'max_margin_percent')
    def _compute_recommended_price(self):
        """Compute recommended price based on strategy (PLACEHOLDER - no real algorithm)"""
        for record in self:
            # PLACEHOLDER: This would use actual cost data in production
            record.recommended_price = 0.0

    @api.constrains('min_margin_percent', 'max_margin_percent')
    def _check_margins(self):
        """Ensure min < max"""
        for record in self:
            if record.min_margin_percent > record.max_margin_percent:
                raise ValueError('Minimum margin must be less than maximum margin.')

    @api.constrains('min_margin_percent', 'max_margin_percent')
    def _check_margin_range(self):
        """Ensure margins are between 0 and 100"""
        for record in self:
            if record.min_margin_percent < 0 or record.max_margin_percent > 100:
                raise ValueError('Margins must be between 0 and 100.')
