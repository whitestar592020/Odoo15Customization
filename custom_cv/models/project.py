from odoo import models, fields


class Project(models.Model):
    _name = "project"
    _description = "Project"
    _table = "project"

    name = fields.Char(string="Name")
    type = fields.Char(string="Type")
    link = fields.Char(string="Link")
    description = fields.Text(string="Description")

    custom_cv_id = fields.Many2one(string="Related CV", comodel_name="custom.cv")
