from odoo import api, models, fields

class CafeCustomer(models.Model):
    _name = 'cafe.customer'
    _description = 'Cafe Customers'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    email = fields.Char(string='Email Address', tracking=True)
    address = fields.Text(string='Address', tracking=True)

    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline",
                                store=True)

    # @api.depends("create_date", "validity")
    # def _compute_date_deadline(self):
    #     for offer in self:
    #         create_date = offer.create_date or fields.Date.today()
    #         offer.date_deadline = create_date + timedelta(days=offer.validity)
    #
    # def _inverse_date_deadline(self):
    #     for offer in self:
    #         if offer.create_date:
    #             offer.validity = (offer.date_deadline - offer.create_date.date()).days
    #         else:
    #             offer.validity = (offer.date_deadline - fields.Date.today()).days
