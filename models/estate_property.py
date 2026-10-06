from odoo import fields, models, api

class EstateProperty(models.Model):
    _name = 'estate.property'   #TECHNICAL OF NAME IN DATABASE
    _description = 'Estate Property'

    state = fields.Selection(
        [('new', 'New'),
        ('booked', 'Booked'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled')],
        default = 'new',
    )

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float(
        string = "selling Price",
        compute = "_compute_selling_price"
    )
    living_area = fields.Integer()
    bedrooms = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [('north', 'North'),
         ('south', 'South'),
         ('east', 'East'),
         ('west', 'West')
         ]
    )

  
    def action_sold(self):
        for record in self:
            record.state = 'sold'
        return True

    def action_booked(self):
        for record in self:
            record.state = 'booked'  
        return True  

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
        return True

    @api.depends('expected_price', 'bedrooms')
    def _compute_selling_price(self):
       for price in self:
          price.selling_price = price.expected_price * price.bedrooms
