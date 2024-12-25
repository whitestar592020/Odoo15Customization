from odoo import models, fields


class Paper(models.Model):
    _name = "paper"
    _description = "Paper"
    _table = "paper"

    name = fields.Char(string="Name", required=True)
    file = fields.Binary(string="File")
    custom_cv_id = fields.Many2one(string="Related CV", comodel_name="custom.cv")
