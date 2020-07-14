# -*- coding: utf-8 -*-
# from odoo import http


# class Devoir4(http.Controller):
#     @http.route('/devoir4/devoir4/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/devoir4/devoir4/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('devoir4.listing', {
#             'root': '/devoir4/devoir4',
#             'objects': http.request.env['devoir4.devoir4'].search([]),
#         })

#     @http.route('/devoir4/devoir4/objects/<model("devoir4.devoir4"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('devoir4.object', {
#             'object': obj
#         })
