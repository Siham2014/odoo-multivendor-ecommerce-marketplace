from odoo import models, fields, api


class ElysiumShopVendor(models.Model):
    """
    Vendor profile model for ElysiumShop marketplace.
    Uses delegated inheritance from res.partner to avoid duplication.
    """
    _name = 'elysiumshop.vendor'
    _description = 'ElysiumShop Vendor'
    _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        required=True,
        ondelete='cascade',
        tracking=True,
        help='Link to res.partner for contact info, address, etc.'
    )
    
    user_id = fields.Many2one(
        'res.users',
        string='Owner User',
        required=True,
        tracking=True,
        help='The Odoo user who owns/manages this vendor account'
    )
    
    vendor_description = fields.Text(
        string='Vendor Description',
        help='Business description and vendor terms'
    )
    
    status = fields.Selection(
        string='Status',
        selection=[
            ('active', 'Active'),
            ('suspended', 'Suspended'),
            ('banned', 'Banned'),
        ],
        default='active',
        tracking=True,
        help='Vendor account status on the marketplace'
    )
    
    commission_rate = fields.Float(
        string='Commission Rate (%)',
        default=10.0,
        help='Commission percentage the marketplace takes from each sale (0-100)'
    )
    
    payout_bank_account = fields.Char(
        string='Payout Bank Account',
        help='Bank account details for vendor payouts'
    )
    
    total_sales = fields.Float(
        string='Total Sales',
        compute='_compute_total_sales',
        help='Sum of all sales from this vendor'
    )
    
    product_count = fields.Integer(
        string='Product Count',
        compute='_compute_product_count',
        help='Number of products sold by this vendor'
    )
    
    avg_rating = fields.Float(
        string='Average Rating',
        compute='_compute_avg_rating',
        help='Average rating from customer reviews'
    )
    
    created_date = fields.Date(
        string='Vendor Created Date',
        default=fields.Date.today,
        tracking=True,
    )
    
    @api.depends('partner_id')
    def _compute_total_sales(self):
        """Compute total sales amount for this vendor (sum of order lines where products are sold by this vendor)."""
        for vendor in self:
            # TODO: Rebuild this after implementing order model.
            # For now, set to 0 as a safe placeholder.
            # This will be implemented in the sales module when order-vendor linkage is properly configured.
            vendor.total_sales = 0.0
            
            # Future implementation (commented):
            # Find all sale order lines where:
            # - The order is in 'sale' or 'done' state
            # - The product's template has this vendor as the seller
            # lines = self.env['sale.order.line'].search([
            #     ('order_id.state', 'in', ['sale', 'done']),
            #     ('product_id.product_tmpl_id.seller_id', '=', vendor.id),
            # ])
            # vendor.total_sales = sum(lines.mapped('price_total'))
    
    @api.depends('partner_id')
    def _compute_product_count(self):
        """Count active products for this vendor."""
        for vendor in self:
            vendor.product_count = self.env['product.template'].search_count([
                ('seller_id', '=', vendor.id),
                ('active', '=', True),
            ])
    
    @api.depends()
    def _compute_avg_rating(self):
        """Compute average rating for this vendor from product reviews."""
        for vendor in self:
            # This will be enhanced once reviews/ratings module is integrated
            vendor.avg_rating = 0.0
    
    def action_open_products(self):
        """Action to open vendor products in tree view."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [('seller_id', '=', self.id)],
            'context': {'default_seller_id': self.id},
        }
    
    def action_deactivate(self):
        """Deactivate vendor by setting status to suspended."""
        self.write({'status': 'suspended'})
    
    def action_activate(self):
        """Activate vendor by setting status to active."""
        self.write({'status': 'active'})
