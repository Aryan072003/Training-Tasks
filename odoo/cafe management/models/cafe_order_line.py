from odoo import api, fields, models

class CafeOrderLine(models.Model):
    _name = 'cafe.order.line'
    _description = 'Cafe Order Line'

    order_id = fields.Many2one('cafe.order', string="Order", readonly=True, ondelete='cascade', index=True, copy=False)
    product_id = fields.Many2one('product.template', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    tax = fields.Float(string='Tax', compute='_compute_tax')
    unit_price = fields.Float(string='Unit Price', compute='_compute_total')
    total = fields.Float(string='Amount', compute='_compute_total')

    @api.depends('product_id', 'quantity')
    def _compute_total(self):
        for product in self:
            product.unit_price = product.product_id.list_price
            product.total = product.product_id.list_price * product.quantity

    @api.depends('product_id')
    def _compute_tax(self):
        for product in self:
            product.tax = sum(product.product_id.taxes_id.mapped('amount'))
