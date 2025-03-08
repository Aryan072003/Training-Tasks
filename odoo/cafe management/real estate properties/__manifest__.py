# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': '',
    'sequence': 10,
    'description': """""",
    'data': [
        'security/ir.model.access.csv',
        'data/estate_sequence.xml',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/offer_line_view.xml',
        'views/real_estate_menu.xml',
    ],
    'depends': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
