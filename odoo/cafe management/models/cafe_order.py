from odoo import api, models, fields, _


class CafeOrder(models.Model):
    _name = 'cafe.order'
    _description = 'Cafe Orders'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Date(string='Order Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string="State", default='draft', tracking=True)
    product_id = fields.Many2one('product.template', string='Product')
    customer_id = fields.Many2one('cafe.customer', string='Customer')
    partner_id = fields.Many2one('res.partner', string='Customer')
    order_line = fields.One2many(
        comodel_name='cafe.order.line',
        inverse_name='order_id',
        string="Order Lines"
    )
    name = fields.Char(string="Order Reference", readonly=True, default=lambda self: _('New'))
    note = fields.Html(
        string="Note",
        store=True, readonly=False, precompute=True)
    amount = fields.Float(string='Total Amount', readonly=True, compute='_compute_amount', tracking=True)
    taxes = fields.Float(string='Total Tax', readonly=True, compute='_compute_amount')
    order_line_id = fields.One2many('cafe.order.line', 'order_id', string='Order Lines')
    invoice_id = fields.Many2one('account.move', string='Invoice')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cafe_order_sequence')
        return super(CafeOrder, self).create(vals)

    def action_cancel(self):
        self.state = 'cancel'

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        if self.state not in ['cancel', 'draft']:
            self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    @api.depends('order_line_id.quantity', 'order_line_id.total')
    def _compute_amount(self):
        for order in self:
            total_amount = 0
            total_tax = 0
            for line in order.order_line_id:
                total_amount += line.total
                total_tax = total_amount * (line.tax / 100)
            order.taxes = total_tax
            order.amount = total_amount + order.taxes

    def create_cafe_invoices(self):
        invoice = self.env['account.move'].create({
            'partner_id': self.partner_id.id,
            'invoice_date': self.date,
            'move_type': 'out_invoice',
            'state': 'draft',
             'invoice_line_ids': [(0, 0, {'product_id': line.product_id.id,
                             'price_unit': line.unit_price,
                             'price_subtotal': line.total,
                             'tax_ids': [line.product_id.taxes_id.id],
                             'quantity': line.quantity,
                             'account_id': 1,
                             }
                      ) for line in self.order_line],
        })
        self.invoice_id = invoice.id
        print(f"invoice : {invoice.id}")
        a = self
