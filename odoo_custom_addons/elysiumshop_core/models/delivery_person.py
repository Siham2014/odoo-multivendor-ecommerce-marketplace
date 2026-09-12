from odoo import models, fields, api
from odoo.exceptions import UserError


class ElysiumShopDeliveryPerson(models.Model):
    """
    Delivery Person (Livreur) model for ElysiumShop marketplace.
    Uses delegated inheritance from res.partner to avoid field duplication.
    """
    _name = 'elysiumshop.delivery.person'
    _description = 'ElysiumShop Delivery Person'
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
        string='Portal User',
        required=True,
        tracking=True,
        help='Odoo user account for portal access and task assignment'
    )
    
    status = fields.Selection(
        string='Delivery Status',
        selection=[
            ('available', 'Available'),
            ('busy', 'Busy'),
            ('inactive', 'Inactive'),
        ],
        default='available',
        tracking=True,
        help='Current availability status of this delivery person'
    )
    
    vehicle_type = fields.Selection(
        string='Vehicle Type',
        selection=[
            ('bike', 'Bike'),
            ('motorcycle', 'Motorcycle'),
            ('car', 'Car'),
            ('van', 'Van'),
            ('truck', 'Truck'),
        ],
        default='bike',
        help='Type of vehicle used for deliveries'
    )
    
    vehicle_plate = fields.Char(
        string='Vehicle License Plate',
        help='Registration plate of delivery vehicle'
    )
    
    zone = fields.Char(
        string='Delivery Zone',
        help='Geographic zone or region where this person operates'
    )
    
    service_area_ids = fields.Many2many(
        'res.country.state',
        'delivery_person_state_rel',
        'delivery_person_id',
        'state_id',
        string='Service Areas (States)',
        help='States/provinces where this delivery person operates'
    )
    
    total_deliveries = fields.Integer(
        string='Total Deliveries',
        compute='_compute_total_deliveries',
        help='Total number of deliveries completed'
    )
    
    avg_rating = fields.Float(
        string='Average Rating',
        compute='_compute_avg_rating',
        help='Average rating from customer delivery feedback'
    )
    
    on_duty = fields.Boolean(
        string='On Duty',
        default=False,
        tracking=True,
        help='Current on-duty status'
    )
    
    created_date = fields.Date(
        string='Account Created Date',
        default=fields.Date.today,
        tracking=True,
    )
    
    @api.depends('user_id')
    def _compute_total_deliveries(self):
        """Count completed deliveries for this person."""
        for person in self:
            # TODO: replace this placeholder when the elysiumshop.delivery.task model is implemented
            # For now, we set total_deliveries to 0 to avoid runtime errors on non-existent model
            person.total_deliveries = 0
    
    @api.depends()
    def _compute_avg_rating(self):
        """Compute average rating for this delivery person."""
        for person in self:
            # This will be enhanced once rating/feedback system is integrated
            person.avg_rating = 0.0
    
    def action_toggle_on_duty(self):
        """Toggle delivery person on-duty status."""
        self.ensure_one()
        self.write({'on_duty': not self.on_duty})
    
    def action_deactivate(self):
        """Deactivate delivery person by setting status to inactive."""
        self.write({'status': 'inactive'})
    
    def action_activate(self):
        """Activate delivery person by setting status to available."""
        self.write({'status': 'available'})
    
    def action_open_tasks(self):
        """Action to open delivery tasks assigned to this person."""
        # TODO: implement delivery task management in the marketplace_delivery module
        # For now, raise a friendly error indicating this feature is not yet available
        raise UserError(
            "Delivery tasks are not implemented yet.\n"
            "This feature will be available in the elysiumshop_delivery module."
        )
