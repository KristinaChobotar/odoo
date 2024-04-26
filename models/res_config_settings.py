from odoo import fields, models

class CompanyNewPostConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    key_API=fields.Char(string='Ключ API', check_company=True, related='company_id.key_API', readonly=False)
    adress_API=fields.Char(string='Адреса API', check_company=True, related='company_id.adress_API', readonly=False)