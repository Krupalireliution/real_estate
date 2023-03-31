# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real Estate',
    'version': '1.1',
    'category': '',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/real_estate_views.xml',
        'views/properties_type.xml',
        'views/properties_tags.xml',
        'views/properties_offers.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
