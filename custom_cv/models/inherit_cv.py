from odoo import models, fields


class InheritCV(models.Model):
    _inherit = "standard.cv"

    is_favorite = fields.Boolean(string="Is Favorite")
    biography = fields.Text(string="Biography")

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")

    marital = fields.Selection(selection_add=[
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ])

    state = fields.Selection(selection_add=[
        ('seek', 'Seeking'),
        ('done',)
    ])

    def action_seek(self):
        for record in self:
            record.state = "seek"
