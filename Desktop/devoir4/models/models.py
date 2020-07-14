# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class devoir4(models.Model):
  _name = 'devoir4.devoir4'


  _inherit = 'stock.picking'


def action_facturation(self):
    self.write({'account.invoice'})


