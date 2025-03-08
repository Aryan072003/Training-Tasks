# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Cafe',
    'version': '1.0',
    'summary': '',
    'sequence': 10,
    'description': """""",
    'data': [
        'security/ir.model.access.csv',
        'views/products_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
        'views/cafe_menu.xml',
        'data/cafe_order_sequence.xml',
    ],
    'depends': ['product', 'mail','account'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
