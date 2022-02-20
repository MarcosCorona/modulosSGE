# -*- coding: utf-8 -*-
# from odoo import http


# class Horarios(http.Controller):
#     @http.route('/horarios/horarios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/horarios/horarios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('horarios.listing', {
#             'root': '/horarios/horarios',
#             'objects': http.request.env['horarios.horarios'].search([]),
#         })

#     @http.route('/horarios/horarios/objects/<model("horarios.horarios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('horarios.object', {
#             'object': obj
#         })
