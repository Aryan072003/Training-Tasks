from odoo import api, fields, models

class PropertyCustomer(models.Model):
    _inherit = 'res.users'
    _description = 'Property Customers'

class PropertyBuyer(models.Model):
    _inherit = 'res.partner'
    _description = 'Property Buyers'