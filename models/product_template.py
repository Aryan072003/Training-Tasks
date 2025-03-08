from odoo import api, models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    customer_id = fields.Many2one('cafe.customer', string='Customer')

