from odoo import fields, models

class Vehicle(models.Model):
	_name = "vehicles.amg"
	_description = "Vehicles personalitzats"

	matricula = fields.Char(required = True)
	marca = fields.Char(string="Marca")
	model = fields.Char(string="Model")
	any = fields.Integer(string="Any de Matriculació")
	kilometres = fields.Float(string="Kilometres Fets")
	itv_vigent = fields.Boolean(string="ITV Vigent")
	propietari = fields.Char(string="Propietari")
	dni_propietari = fields.Char(string="DNI del Propietari", size=9)

