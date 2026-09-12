# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MarketplaceDeliveryRoute(models.Model):
    _name = 'marketplace.delivery.route'
    _description = 'Delivery Route'
    _order = 'date desc'

    name = fields.Char(string='Route Name', required=True)
    delivery_person = fields.Many2one(
        'res.partner',
        string='Delivery Person',
        required=True,
        domain=[('is_company', '=', False)]
    )
    task_ids = fields.One2many(
        'marketplace.delivery.task',
        'route_id',
        string='Delivery Tasks'
    )
    date = fields.Date(string='Route Date', required=True, default=fields.Date.today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Done'),
    ], string='Status', default='draft', required=True)
    total_tasks = fields.Integer(
        string='Total Tasks',
        compute='_compute_total_tasks',
        store=False
    )
    completed_tasks = fields.Integer(
        string='Completed Tasks',
        compute='_compute_completed_tasks',
        store=False
    )

    @api.depends('task_ids')
    def _compute_total_tasks(self):
        for record in self:
            record.total_tasks = len(record.task_ids)

    @api.depends('task_ids')
    def _compute_completed_tasks(self):
        for record in self:
            record.completed_tasks = len(record.task_ids.filtered(lambda t: t.status == 'delivered'))

    def action_activate(self):
        self.state = 'active'

    def action_complete(self):
        self.state = 'done'
