from odoo import models, fields, api


class Type(models.Model):
    _name = 'estate.property.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Type estate"
    
    property_ids = fields.One2many("estate", "property_type_id", string="Properties")
