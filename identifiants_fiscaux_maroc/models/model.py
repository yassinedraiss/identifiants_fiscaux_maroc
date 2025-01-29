
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    rc = fields.Char(string='RC')
    tp = fields.Char(string='TP')
    iff = fields.Char(string='IF')
    cnss = fields.Char(string='CNSS')
    ice = fields.Char(string='ICE' )
    capital = fields.Char(string='Capital')
    cin = fields.Char(string='CIN')

  
   
        

class ResCompany(models.Model):
    _inherit = 'res.company'

    rc = fields.Char(string='RC')
    tp = fields.Char(string='TP')
    iff = fields.Char(string='IF')
    cnss = fields.Char(string='CNSS')
    ice = fields.Char(string='ICE')
    capital = fields.Char(string='Capital')

