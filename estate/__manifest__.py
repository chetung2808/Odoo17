# -*- coding: utf-8 -*-
{
    'name': "Exsercise",

    'summary': """
        Trainning odoo"
    """,

    'description': """
        Trainning odoo"
    """,

    'author': "Tung",
    'website': "https://www.odoo.com",
    'category': 'Tutorials/AwesomeOwl',
    'version': '0.1',

    'depends': ['base','mail'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_template.xml',
        'views/estate_property_type.xml',
        'views/owl.xml',
    ],
    'assets': {  
            'images': ['static/description/icon.png'],
            "web.assets_backend": [
                "test/static/src/js/estate_list.js",
                "test/static/src/xml/estate_list.xml",
            ],
    },
    'license': 'AGPL-3'
}
