from odoo import models, fields, api, _
import datetime
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment')
    ])
    state = fields.Selection([
        ('draft', 'Available'),
        ('sold', 'Sold'),
        ('cancel', 'Cancelled')
    ], string="State", default='draft', tracking=True)
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', default=datetime.datetime.today())
    expected_price = fields.Float(string='Expected Price', required=True)
    best_price = fields.Float(string='Best Price', compute='_compute_best_price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms', default=3)
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area(sqm)')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')
    total_area = fields.Integer(string='Total Area(sqm)', compute='_compute_total_area')
    ref = fields.Char(string="Order Reference", readonly=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('res.users', string='Customers')
    buyer_id = fields.Many2one('res.partner', string='Buyer', compute='_compute_buyer')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    offer_line = fields.One2many('offer.line', 'property_id', string='Offers')

    _sql_constraints = [('positive_price', 'CHECK(expected_price > 0.0)', 'Price must be positive')]

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('estate_sequence')
        return super(EstateProperty, self).create(vals)

    def action_sold(self):
        if self.state == 'cancel':
            raise UserError(_('Cancelled properties cannot be sold'))
        self.state = 'sold'

    def action_available(self):
        self.state = 'draft'

    def action_cancel(self):
        if self.state == 'sold':
            raise UserError(_('Sold properties cannot be cancelled'))
        self.state = 'cancel'

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        self.total_area = self.living_area + self.garden_area

    @api.onchange('garden')
    def _onchange_garden(self):
        if not self.garden:
            self.garden_area = 0

    @api.depends('offer_line')
    def _compute_best_price(self):
        for record in self:
            price_best = 0
            for line in record.offer_line:
                if line.status == 'accept':
                    price_best = line.price
            record.best_price = price_best
            record.selling_price = record.best_price

    def _compute_buyer(self):
        for record in self:
            buyer = ''
            for line in record.offer_line:
                if line.status == 'accept':
                    buyer = line.partner
            record.buyer_id = buyer
            break