# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MarketplaceVendor(models.Model):
    _name = 'marketplace.vendor'
    _description = 'Marketplace Vendor Profile'
    _inherits = {'res.partner': 'vendor_partner_id'}

    vendor_partner_id = fields.Many2one(
        'res.partner',
        string='Vendor Partner',
        required=True,
        ondelete='cascade',
        delegate=True
    )
    is_vendor = fields.Boolean(
        string='Is Vendor',
        default=True
    )
    commission_rate = fields.Float(
        string='Commission Rate (%)',
        default=10.0,
        help='Commission percentage on vendor sales'
    )
    status = fields.Selection(
        [
            ('active', 'Active'),
            ('suspended', 'Suspended'),
            ('banned', 'Banned')
        ],
        string='Vendor Status',
        default='active',
        required=True
    )
    total_products = fields.Integer(
        string='Total Products',
        compute='_compute_total_products',
        readonly=True
    )
    total_sales = fields.Float(
        string='Total Sales',
        compute='_compute_total_sales',
        readonly=True
    )
    return_rate = fields.Float(
        string='Return Rate (%)',
        compute='_compute_return_rate',
        readonly=True
    )
    description = fields.Text(
        string='Description',
        help='Detailed vendor description'
    )
    product_ids = fields.One2many(
        'marketplace.vendor.product',
        'vendor_id',
        string='Vendor Products'
    )
    payout_ids = fields.One2many(
        'marketplace.vendor.payout',
        'vendor_id',
        string='Vendor Payouts'
    )

    @api.depends('product_ids')
    def _compute_total_products(self):
        """Compute total number of products for this vendor"""
        for vendor in self:
            vendor.total_products = len(vendor.product_ids)

    @api.depends('product_ids')
    def _compute_total_sales(self):
        """Compute total sales - placeholder returns 0"""
        for vendor in self:
            vendor.total_sales = 0.0

    @api.depends('product_ids')
    def _compute_return_rate(self):
        """Compute return rate - placeholder returns 0"""
        for vendor in self:
            vendor.return_rate = 0.0

    @api.onchange('vendor_partner_id')
    def _onchange_vendor_partner_id(self):
        """Auto-populate vendor fields from partner"""
        if self.vendor_partner_id:
            self.name = self.vendor_partner_id.name
            self.email = self.vendor_partner_id.email
            self.phone = self.vendor_partner_id.phone
            self.is_company = True

    def action_activate_vendor(self):
        """Activate vendor"""
        self.write({'status': 'active'})

    def action_suspend_vendor(self):
        """Suspend vendor"""
        self.write({'status': 'suspended'})

    def action_ban_vendor(self):
        """Ban vendor"""
        self.write({'status': 'banned'})
