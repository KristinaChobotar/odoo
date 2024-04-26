from odoo import fields, models

class CompanyNewPost(models.Model):
    _inherit = 'res.company'

    key_API=fields.Char(string='Ключ API', required=True)
    adress_API=fields.Char(string='Адреса API', required=True)