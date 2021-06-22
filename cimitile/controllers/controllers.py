# -*- coding: utf-8 -*-
# from odoo import http


# class Cimitile(http.Controller):
#     @http.route('/cimitile/cimitile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cimitile/cimitile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cimitile.listing', {
#             'root': '/cimitile/cimitile',
#             'objects': http.request.env['cimitile.cimitile'].search([]),
#         })

#     @http.route('/cimitile/cimitile/objects/<model("cimitile.cimitile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cimitile.object', {
#             'object': obj
#         })
