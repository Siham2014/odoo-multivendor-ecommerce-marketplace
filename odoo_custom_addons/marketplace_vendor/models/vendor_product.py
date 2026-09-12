# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MarketplaceVendorProduct(models.Model):
    _name = 'marketplace.vendor.product'
    _description = 'Marketplace Vendor Product'
    _order = 'create_date DESC'

    vendor_id = fields.Many2one(
        'marketplace.vendor',
        string='Vendor',
        required=True,
        ondelete='cascade'
    )
    product_id = fields.Many2one(
        'product.template',
        string='Product',
        required=True,
        ondelete='cascade'
    )
    price = fields.Float(
        string='Vendor Price',
        required=True,
        digits='Product Price'
    )
    quantity_available = fields.Float(
        string='Available Quantity',
        default=0.0
    )
    is_active = fields.Boolean(
        string='Active',
        default=True
    )
    total_sales = fields.Float(
        string='Total Sales',
        compute='_compute_total_sales',
        readonly=True
    )
    creation_date = fields.Datetime(
        string='Creation Date',
        readonly=True,
        default=fields.Datetime.now
    )

    @api.depends('product_id')
    def _compute_total_sales(self):
        """Compute total sales - placeholder returns 0"""
        for record in self:
            record.total_sales = 0.0

    @api.constrains('price')
    def _check_price(self):
        """Ensure price is positive"""
        for record in self:
            if record.price < 0:
                raise models.ValidationError('Price cannot be negative')

    @api.constrains('quantity_available')
    def _check_quantity(self):
        """Ensure quantity is positive"""
        for record in self:
            if record.quantity_available < 0:
                raise models.ValidationError('Quantity cannot be negative')
