# -*- coding: utf-8 -*-
# from odoo import http


# class EditionEcheancier(http.Controller):
#     @http.route('/edition_echeancier/edition_echeancier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edition_echeancier/edition_echeancier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edition_echeancier.listing', {
#             'root': '/edition_echeancier/edition_echeancier',
#             'objects': http.request.env['edition_echeancier.edition_echeancier'].search([]),
#         })

#     @http.route('/edition_echeancier/edition_echeancier/objects/<model("edition_echeancier.edition_echeancier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edition_echeancier.object', {
#             'object': obj
#         })
