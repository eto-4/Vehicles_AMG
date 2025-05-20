from odoo import fields, models

class Vehicle(models.Model):
	_name = "vehicles.amg"
	_description = "Vehicles personalitzats"

	matricula = fields.Char("Matricula", required = True)
	marca = fields.Char("Marca")
	model = fields.Char("Model")
	any = fields.Integer("Any de Matriculació")
	kilometres = fields.Float("Kilometres Fets")
	itv_vigent = fields.Boolean("ITV Vigent")
	propietari = fields.Char("Propietari")
	dni_propietari = fields.Char("DNI del Propietari", size=9)

