# -*- coding: utf-8 -*-


from odoo import api, models, fields, _ 




class Company(models.Model):
    _inherit = 'res.company'


    municipality_id = fields.Many2one('res.country.state.municipality', 'Municipality')
    parish_id = fields.Many2one('res.country.state.municipality.parish', 'Parish')


