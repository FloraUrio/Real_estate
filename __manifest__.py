#-*_ coding: utf-8 -*-

{
    'name': 'Real Estate',
    'description': 'Real Estate Management',
    'application': True,
    'author': 'Odoo F.U',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
       
    ],
    'installable': True,
    'sequence': 5
}