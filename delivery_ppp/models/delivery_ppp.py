# -*- coding: utf-8 -*-
from odoo import models, fields

class pickuplocationproviderPPP(models.Model):
    _inherit = "delivery.carrier"

    pickup_location_provider = fields.Selection([('ppp',"Pick Pack Pont")], string='Pickup location provider', required=False)
    
class saleorderpickuplocation(models.Model):
    _inherit = "sale.order"

    pickup_location = fields.Char("PPP Boltkód")
    pickup_address = fields.Char("PPP Bolt cím")
    pickup_name = fields.Char("PPP Bolt név")