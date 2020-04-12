# -*- coding: utf-8 -*-
{
    'name' : 'Pick Pack Pont',
    'version' : '1.0',
    'summary': 'Pick Pack Pont Addon',
    'sequence': 1,
    'description': """
Pick Pack Pont
    """,
    'category': 'Other',
    'website': 'https://www.eyssen.hu',
    'depends' : ['website_sale', 'delivery', 'website_sale_delivery'],
    'data': [
        'data/delivery_ppp_data.xml',
        'views/website_sale_delivery_ppp_template.xml',
        'views/sale_order.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}