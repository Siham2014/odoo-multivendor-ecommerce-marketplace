# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta


class MarketplaceVendorPayout(models.Model):
    _name = 'marketplace.vendor.payout'
    _description = 'Marketplace Vendor Payout'
    _order = 'create_date DESC'

    name = fields.Char(
        string='Payout Reference',
        required=True,
        readonly=True,
        default='/'
    )
    vendor_id = fields.Many2one(
        'marketplace.vendor',
        string='Vendor',
        required=True,
        ondelete='cascade'
    )
    amount = fields.Float(
        string='Payout Amount',
        required=True,
        digits='Account'
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('approved', 'Approved'),
            ('paid', 'Paid')
        ],
        string='Status',
        default='draft',
        required=True
    )
    scheduled_date = fields.Date(
        string='Scheduled Payout Date',
        required=True
    )
    payment_reference = fields.Char(
        string='Payment Reference',
        readonly=True
    )
    notes = fields.Text(
        string='Notes'
    )
    create_date = fields.Datetime(
        string='Created Date',
        readonly=True
    )

    @api.model
    def create(self, vals):
        """Generate sequence on creation"""
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('marketplace.vendor.payout') or '/'
        return super().create(vals)

    @api.constrains('amount')
    def _check_amount(self):
        """Ensure amount is positive"""
        for record in self:
            if record.amount <= 0:
                raise models.ValidationError('Payout amount must be greater than 0')

    def action_approve_payout(self):
        """Approve payout"""
        self.write({'state': 'approved'})

    def action_mark_paid(self):
        """Mark payout as paid"""
        for record in self:
            record.write({
                'state': 'paid',
                'payment_reference': f"PAY-{record.vendor_id.id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            })

    def action_reset_draft(self):
        """Reset payout to draft"""
        self.write({'state': 'draft', 'payment_reference': ''})
