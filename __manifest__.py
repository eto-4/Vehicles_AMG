{
	'name': 'Vehicles Management',
	'description': """Mòdul per gestionar la flota de vehicles de l\'empresa""",
	'category': 'Fleet Management',
	'version': '1.0',
	'depends': ['base'],
	'data': [
		'data/vehicles_data.csv',
		'security/ir.model.access.csv',
		'views/vehicle_view.xml',
		# 'views/menu_view.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False
}