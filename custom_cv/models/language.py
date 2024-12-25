from odoo import models, fields


class Language(models.Model):
    _name = "language"
    _description = "Language"
    _table = "language"

    name = fields.Char(string="Language", required=True)
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Language already exists!")
    ]


class LanguageLine(models.Model):
    _name = "language.line"
    _description = "Language Line"
    _table = "language_line"

    language_id = fields.Many2one(string="Language", comodel_name="language", required=True)
    level = fields.Selection([
        ('basic', 'Basic'),
        ('inter', 'Intermediate'),
        ('advan', 'Advanced')
    ], string="Language Level", default="basic")

    def _compute_progress(self):
        for record in self:
            if record.level == 'basic':
                record.progress = 20
            elif record.level == 'inter':
                record.progress = 60
            else:
                record.progress = 100

    progress = fields.Integer(string="Progress", compute=_compute_progress)

    custom_cv_id = fields.Many2one(string="Related CV", comodel_name="custom.cv")
