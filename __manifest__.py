# -*- coding: utf-8 -*-
{
    'name':'Нова Пошта',
    'version':'17.0.0.0.0',
    'summary': 'Delivery',
	'category': 'Tools',
	'author': 'Kristina Chobotar',
	'maintainer': 'Economic Cybernetics',
	'company': '',
	'website': '',
	'depends': ['base'],
	'data': [
		'security/ir.model.access.csv',
		'views/delivery_view.xml',
		'data/new_post_update.xml',
        'data/cron_data.xml'
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': False,
	'auto_install': False,
}