from odoo import models, fields


class Office(models.Model):
    _name = 'office.employee'

    name = fields.Many2one('res.partner',string='Employee')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')