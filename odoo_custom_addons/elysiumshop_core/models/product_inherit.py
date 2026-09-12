from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    """
    Extend product.template to add seller/vendor information.
    Links products to vendors for marketplace catalog.
    """
    _inherit = 'product.template'

    seller_id = fields.Many2one(
        'elysiumshop.vendor',
        string='Vendor',
        tracking=True,
        help='The vendor/seller who offers this product'
    )
    
    vendor_sku = fields.Char(
        string='Vendor SKU',
        help='Vendor-specific product code/reference'
    )
    
    is_marketplace_product = fields.Boolean(
        string='Marketplace Product',
        default=False,
        tracking=True,
        help='Whether this product is sold on the ElysiumShop marketplace'
    )
    
    commission_amount = fields.Float(
        string='Commission Amount',
        compute='_compute_commission_amount',
        help='Marketplace commission per sale (computed from vendor rate)'
    )
    
    @api.depends('seller_id', 'list_price')
    def _compute_commission_amount(self):
        """
        Compute commission amount based on vendor's commission rate
        and product price.
        """
        for product in self:
            if product.seller_id:
                product.commission_amount = (
                    product.list_price * product.seller_id.commission_rate / 100.0
                )
            else:
                product.commission_amount = 0.0
