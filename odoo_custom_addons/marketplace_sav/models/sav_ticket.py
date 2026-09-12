from odoo import models, fields, api
from odoo.exceptions import UserError


class SavTicket(models.Model):
    _name = 'sav.ticket'
    _description = 'Service Après Vente Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date DESC'

    # Fields
    name = fields.Char(
        string='Ticket Number',
        default='New',
        readonly=True,
        tracking=True,
    )

    order_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        required=True,
        tracking=True,
        help='Original sales order for this item'
    )

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
        tracking=True,
        help='Product being claimed'
    )

    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        tracking=True,
        help='Customer who submitted the claim'
    )

    reason = fields.Selection(
        string='Reason for Claim',
        selection=[
            ('defect', 'Product Defect'),
            ('damaged', 'Damaged on Arrival'),
            ('missing_parts', 'Missing Parts'),
            ('wrong_item', 'Wrong Item Received'),
            ('not_working', 'Not Working as Described'),
            ('quality_issue', 'Quality Issue'),
            ('other', 'Other'),
        ],
        required=True,
        tracking=True,
        help='Reason for opening this SAV ticket'
    )

    description = fields.Text(
        string='Description',
        help='Detailed description of the issue'
    )

    image = fields.Binary(
        string='Image',
        help='Image of the defected product'
    )

    state = fields.Selection(
        string='Status',
        selection=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('assigned', 'Assigned'),
            ('in_progress', 'In Progress'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('refunded', 'Refunded'),
            ('closed', 'Closed'),
        ],
        default='draft',
        tracking=True,
        help='Current status of this ticket'
    )

    responsible_id = fields.Many2one(
        'res.users',
        string='Responsible',
        tracking=True,
        help='SAV manager responsible for this ticket'
    )

    resolution_notes = fields.Text(
        string='Resolution Notes',
        help='Notes on resolution or rejection reason'
    )

    create_date = fields.Datetime(
        string='Created Date',
        readonly=True,
        help='Date when ticket was created'
    )

    # Computed fields
    days_since_creation = fields.Integer(
        string='Days Since Creation',
        compute='_compute_days_since_creation',
        help='Number of days since ticket creation'
    )

    # Sequences
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('sav.ticket')
        return super().create(vals)

    @api.depends('create_date')
    def _compute_days_since_creation(self):
        for ticket in self:
            if ticket.create_date:
                from datetime import datetime
                now = datetime.now()
                delta = now - ticket.create_date.replace(tzinfo=None)
                ticket.days_since_creation = delta.days
            else:
                ticket.days_since_creation = 0

    # Workflow methods
    def button_submit(self):
        """Submit the ticket"""
        self.write({'state': 'submitted'})

    def button_assign(self):
        """Assign ticket to responsible"""
        if not self.responsible_id:
            raise UserError('Please assign a responsible person first')
        self.write({'state': 'assigned'})

    def button_start(self):
        """Start processing ticket"""
        if self.state != 'assigned':
            raise UserError('Ticket must be assigned first')
        self.write({'state': 'in_progress'})

    def button_approve(self):
        """Approve the claim - requires manager"""
        if not self.user_has_groups('marketplace_sav.group_sav_manager'):
            raise UserError('You do not have permission to approve tickets')
        if not self.resolution_notes:
            raise UserError('Please add resolution notes before approving')
        self.write({'state': 'approved'})

    def button_reject(self):
        """Reject the claim - requires manager"""
        if not self.user_has_groups('marketplace_sav.group_sav_manager'):
            raise UserError('You do not have permission to reject tickets')
        if not self.resolution_notes:
            raise UserError('Please add rejection reason before rejecting')
        self.write({'state': 'rejected'})

    def button_refund(self):
        """Refund the customer - requires manager"""
        if not self.user_has_groups('marketplace_sav.group_sav_manager'):
            raise UserError('You do not have permission to refund')
        if self.state != 'approved':
            raise UserError('Only approved tickets can be refunded')
        if not self.resolution_notes:
            raise UserError('Please add refund details before refunding')
        self.write({'state': 'refunded'})

    def button_close(self):
        """Close the ticket"""
        self.write({'state': 'closed'})

    def action_open_order(self):
        """Open the related sales order"""
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': self.order_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.onchange('order_id')
    def _onchange_order_id(self):
        """Auto-populate customer from order"""
        if self.order_id:
            self.customer_id = self.order_id.partner_id
