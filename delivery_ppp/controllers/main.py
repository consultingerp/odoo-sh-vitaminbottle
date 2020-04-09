# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale_delivery.controllers.main import WebsiteSaleDelivery

class delivery_pickup_controller(WebsiteSaleDelivery):


    @http.route(['/shop/set_pickup_location'], type='http', auth="public", website=True)
    def set_pickup_location(self, **post):
        order = request.website.sale_get_order()
        locationid = post.get('locationid')
        address = post.get('address')
        order.write({'pickup_location': locationid, 'pickup_address': address})
        return 'locationid set:' + locationid