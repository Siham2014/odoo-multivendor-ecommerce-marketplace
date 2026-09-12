# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request


class VendorPortalController(http.Controller):

    def _get_current_vendor(self):
        """Get current vendor partner or None"""
        user = request.env.user
        if user.partner_id:
            return user.partner_id
        return None

    def _check_vendor_access(self):
        """Check if user has vendor portal access"""
        user = request.env.user
        if 'vendor_portal_user' not in [g.name for g in user.groups_id]:
            return request.redirect('/web/login')
        return None

    @http.route('/vendor/portal', type='http', auth='user', website=True)
    def vendor_portal_dashboard(self):
        """Vendor Portal Dashboard"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        return request.render('marketplace_vendor_portal.portal_dashboard', {
            'vendor': vendor,
        })

    @http.route('/vendor/products', type='http', auth='user', website=True)
    def vendor_products(self):
        """List vendor products"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        # Get products for this vendor
        products = request.env['product.template'].sudo().search([
            ('company_id', '=', request.env.company.id)
        ])

        return request.render('marketplace_vendor_portal.portal_products', {
            'vendor': vendor,
            'products': products,
        })

    @http.route('/vendor/add-product', type='http', auth='user', website=True)
    def vendor_add_product(self, **post):
        """Add new product form"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        if request.httprequest.method == 'POST':
            # Create product
            try:
                product = request.env['product.template'].sudo().create({
                    'name': post.get('name'),
                    'type': 'product',
                    'list_price': float(post.get('price', 0)),
                    'description': post.get('description'),
                })
                return request.redirect('/vendor/products')
            except Exception as e:
                return request.render('marketplace_vendor_portal.portal_add_product', {
                    'vendor': vendor,
                    'error': str(e),
                })

        return request.render('marketplace_vendor_portal.portal_add_product', {
            'vendor': vendor,
        })

    @http.route('/vendor/orders', type='http', auth='user', website=True)
    def vendor_orders(self):
        """List vendor orders"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        # Get orders
        orders = request.env['sale.order'].sudo().search([
            ('company_id', '=', request.env.company.id)
        ], order='create_date desc')

        return request.render('marketplace_vendor_portal.portal_orders', {
            'vendor': vendor,
            'orders': orders,
        })

    @http.route('/vendor/delivery', type='http', auth='user', website=True)
    def vendor_delivery(self):
        """View delivery status"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        # Get delivery tasks
        try:
            delivery_tasks = request.env['marketplace.delivery.task'].sudo().search([
                ('delivery_person', '=', vendor.id)
            ], order='trigger_datetime desc', limit=50)
        except:
            delivery_tasks = []

        return request.render('marketplace_vendor_portal.portal_delivery', {
            'vendor': vendor,
            'delivery_tasks': delivery_tasks,
        })

    @http.route('/vendor/sav', type='http', auth='user', website=True)
    def vendor_sav_tickets(self):
        """View SAV tickets"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        # Get SAV tickets (if module exists)
        try:
            sav_tickets = request.env['marketplace.sav.ticket'].sudo().search([
                ('state', '!=', 'closed')
            ], order='create_date desc', limit=50)
        except:
            sav_tickets = []

        return request.render('marketplace_vendor_portal.portal_sav', {
            'vendor': vendor,
            'sav_tickets': sav_tickets,
        })

    @http.route('/vendor/notifications', type='http', auth='user', website=True)
    def vendor_notifications(self):
        """View notifications"""
        access_denied = self._check_vendor_access()
        if access_denied:
            return access_denied

        vendor = self._get_current_vendor()
        if not vendor:
            return request.redirect('/web')

        # Get notifications
        try:
            notifications = request.env['marketplace.notification'].sudo().search([
                ('user_id', '=', request.env.user.id)
            ], order='trigger_datetime desc', limit=50)
        except:
            notifications = []

        return request.render('marketplace_vendor_portal.portal_notifications', {
            'vendor': vendor,
            'notifications': notifications,
        })
