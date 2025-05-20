{
	'name': 'Vehicles Management',
	'description': """Mòdul per gestionar la flota de vehicles de l\'empresa""",
	'category': 'Fleet Management',
	'version': '1.0',
	'depends': ['base'],
	'data': [
		'security/ir.model.access.csv',
		'data/vehicles_data.csv',
		'views/vehicle_view.xml',
		'views/menu_view.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False
}