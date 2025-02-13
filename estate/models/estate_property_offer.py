from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class Offer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Offer estate"

    date_deadline = fields.Date(compute="_compute_date_deadline", string="Date deadline", tracking=True, store=True)
    validity = fields.Integer(string="Validity",tracking=True,  default=7)
    state = fields.Selection(
        [
            ('accept', 'Accept'),
            ('pending', 'Pending'),
            ('refuse', 'Refuse'),
        ],
        string="State",
        required=True,
        copy=False,
        default='pending',
        store=True,
        tracking=True,
    )
    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = date.today() + relativedelta(days=record.validity)
    
    
    def ac_accept(self):
        for record in self:
            record.state= 'accept'    
            
    def ac_refuse(self):
        for record in self:
            record.state= 'refuse'     