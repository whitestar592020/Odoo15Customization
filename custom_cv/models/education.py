from odoo import models, fields


class Education(models.Model):
    _name = "education"
    _description = "Education"
    _table = "education"

    name = fields.Char(string="Name", required=True)
    edu_center = fields.Char(string="Education Center")
    description = fields.Text(string="Description")


class EducationLine(models.Model):
    _name = "education.line"
    _description = "Education Line"
    _table = "education_line"

    edu_id = fields.Many2one(string="Certificate",
                             comodel_name="education")
    edu_center = fields.Char(string="Education Center", related="edu_id.edu_center")

    period_from = fields.Date(string="Period From")
    period_to = fields.Date(string="Period To")

    custom_cv_id = fields.Many2one(string="Related CV",
                                   comodel_name="custom.cv")
