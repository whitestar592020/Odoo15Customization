from odoo import models, fields


class Experience(models.Model):
    _name = "experience"
    _description = "Experience"
    _table = "experience"

    name = fields.Char(string="Job Position", required=True)
    company = fields.Char(string="Company")
    description = fields.Text(string="Description")


class ExperienceLine(models.Model):
    _name = "experience.line"
    _description = "Experience Line"
    _table = "experience_line"

    exp_id = fields.Many2one(string="Job Position", comodel_name="experience", required=True)

    company = fields.Char(string="Company", related="exp_id.company")

    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")
    responsibility = fields.Text(string="Responsibility")

    custom_cv_id = fields.Many2one(string="Related CV", comodel_name="custom.cv")
