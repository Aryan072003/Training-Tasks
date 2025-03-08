from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Types'

    name = fields.Char(string='Type')

    _sql_constraints = [('unique_name', 'UNIQUE(name)', 'A property with same name already exists')]