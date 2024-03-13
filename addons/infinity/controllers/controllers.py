# -*- coding: utf-8 -*-
# from odoo import http


# class Infinity(http.Controller):
#     @http.route('/infinity/infinity', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infinity/infinity/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('infinity.listing', {
#             'root': '/infinity/infinity',
#             'objects': http.request.env['infinity.infinity'].search([]),
#         })

#     @http.route('/infinity/infinity/objects/<model("infinity.infinity"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infinity.object', {
#             'object': obj
#         })

