from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CustomCV(models.Model):
    _name = "custom.cv"
    _description = "Custom CV"
    _table = "custom_cv"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Career Name", required=True, translate=True)
    image = fields.Binary(string="Career Image")
    job_title = fields.Char(string="Job Title")

    @api.constrains('name', 'job_title')
    def _check_cv_record(self):
        cv_rec = self.env['custom.cv'].search([
            ('id', '!=', self.id),
            ('name', '=', self.name),
            ('job_title', '=', self.job_title)
        ])
        if cv_rec:
            raise ValidationError(_("CV record is alrealy exist!"))

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if 'job_title' not in default:
            default['job_title'] = "%s (Copy)" % self.job_title
        return super(CustomCV, self).copy(default=default)

    profile = fields.Text(string="Profile")

    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    social = fields.Char(string="Social Media")
    address = fields.Char(string="Address")

    dob = fields.Date(string="Date of Birth")
    nationality = fields.Char(string="Nationality")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married')
    ], string="Marital Status")

    education_line_ids = fields.One2many(string="Related Education",
                                         comodel_name="education.line",
                                         inverse_name="custom_cv_id")

    experience_line_ids = fields.One2many(string="Related Experience",
                                          comodel_name="experience.line",
                                          inverse_name="custom_cv_id")

    project_ids = fields.One2many(string="Related Project",
                                  comodel_name="project",
                                  inverse_name="custom_cv_id")

    language_line_ids = fields.One2many(string="Related Language",
                                        comodel_name="language.line",
                                        inverse_name="custom_cv_id")

    paper_ids = fields.One2many(string="Related Paper",
                                comodel_name="paper",
                                inverse_name="custom_cv_id")

    def action_paper(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Related Paper",
            "res_model": "paper",
            "view_mode": "tree,form",
            "domain": [('id', 'in', self.paper_ids.ids)],
            "context": {'default_custom_cv_id': self.id},
        }

    paper_count = fields.Integer(compute="_compute_paper_count")

    def _compute_paper_count(self):
        Paper = self.env['paper']
        for record in self:
            record.paper_count = Paper.search_count([('custom_cv_id', '=', self.id)])

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('seek', 'Seeking'),
        ('done', 'Done')
    ], string="Status", default="draft")

    def action_confirm(self):
        for record in self:
            if record.job_title:
                record.state = "confirm"
            else:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'danger',
                        'title': 'Job Title is empty!',
                        'message': 'Job Title should be fill...',
                        'sticky': True,
                    }
                }

    def action_seek(self):
        for record in self:
            record.state = "seek"
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Good Luck! You are now seeing the job!',
                'type': 'rainbow_man',
            }
        }

    def action_done(self):
        for record in self:
            record.state = "done"
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Congratulations! Have a good job!',
                'type': 'rainbow_man',
            }
        }

    def action_draft(self):
        for record in self:
            record.state = "draft"

    active = fields.Boolean(string="Active", default=True)
