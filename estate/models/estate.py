from odoo import models,fields,api,_
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class Estate(models.Model):
    _name = "estate"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Estate fields"
        
    name = fields.Char('Name',required=True, tracking=True)
    number_of_months = fields.Integer('# Months',)  
    nums_of_beth  = fields.Integer('number of bedrooms', default=2, tracking=True)
    availability_date = fields.Date("Availability Date", default=lambda self: date.today()+ relativedelta(months=3))  
    partner_id = fields.Many2one("res.partner", string="Partner")
    living_area = fields.Integer('Living area',required=True, tracking=True)
    garden_area = fields.Integer('Garden area',required=True, tracking=True)
    total_area = fields.Integer(compute="_compute_total", store=True,tracking=True)
    best_price = fields.Float("Best Offer", compute="_compute_best_price", help="Best offer received")
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        string="State",
        required=True,
        copy=False,
        default='new',
        store=True,
        tracking=True,
    )
    @api.depends('living_area','garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
        
    @api.constrains('total_area')
    def check_area(self):
        for record in self:
            if record.total_area < 0 :
                raise ValidationError('The min area is 1' )
            
    
    def ac_sold(self):
        if "canceled" in self.mapped("state"):
            raise UserError("This property is Canceled ")
        return self.write({"state": "sold"})
    
    def ac_canceled(self):
        if "sold" in self.mapped("state"):
            raise UserError("This property is Sold ")
        return self.write({"state": "canceled"})
    
