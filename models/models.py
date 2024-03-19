# -*- coding: utf-8 -*-

from odoo import models, fields, api

class stock_picking_ext(models.Model):
    _inherit = 'stock.picking'

    analytic_account_id = fields.Many2one('account.analytic.account')
