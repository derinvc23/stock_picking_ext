# -*- coding: utf-8 -*-
from odoo import http

# class StockPickingExt(http.Controller):
#     @http.route('/stock_picking_ext/stock_picking_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_picking_ext/stock_picking_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_picking_ext.listing', {
#             'root': '/stock_picking_ext/stock_picking_ext',
#             'objects': http.request.env['stock_picking_ext.stock_picking_ext'].search([]),
#         })

#     @http.route('/stock_picking_ext/stock_picking_ext/objects/<model("stock_picking_ext.stock_picking_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_picking_ext.object', {
#             'object': obj
#         })