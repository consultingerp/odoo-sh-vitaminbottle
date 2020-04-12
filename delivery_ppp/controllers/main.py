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
        name = post.get('name')
        order.write({'pickup_location': locationid, 'pickup_address': address, 'pickup_name': name})
        return 'locationid set:' + locationid
    
    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def payment(self, **post):
        order = request.website.sale_get_order()
        carrier_id = post.get('carrier_id')
        if carrier_id:
            carrier_id = int(carrier_id)            
            if order.carrier_id.id != carrier_id:
                order.write({'pickup_location':'', 'pickup_address': ''})
                
        return super(delivery_pickup_controller, self).payment(**post)
    