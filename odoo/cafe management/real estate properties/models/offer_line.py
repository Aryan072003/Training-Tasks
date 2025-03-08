from datetime import timedelta
from odoo import api, fields, models

class OfferLine(models.Model):
    _name = 'offer.line'
    _description = 'Offers for the property'

    property_id = fields.Many2one('estate.property', string='Property')
    price = fields.Float(string='Price')
    partner = fields.Many2one('res.partner', string='Partner')
    status = fields.Selection([
        ('accept', 'Accept'),
        ('refuse','Refuse')
    ], string='Status', readonly=True)
    validity = fields.Integer(string='Validity', default=7)
    deadline = fields.Date(string='Deadline', compute='_compute_deadline', inverse='_inverse_deadline')

    @api.depends('validity','create_date')
    def _compute_deadline(self):
        for record in self:
            if record.create_date and record.validity:
                record.deadline = record.create_date + timedelta(days=record.validity)

    @api.depends('deadline', 'create_date')
    def _inverse_deadline(self):
        for record in self:
            if record.create_date and record.deadline:
                record.validity = (record.deadline - record.create_date.date()).days

    def accept_offer(self):
        for offer in self:
            offer.status = 'accept'

    def refuse_offer(self):
        for offer in self:
            offer.status = 'refuse'


