# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class edition_echeancier(models.Model):
#     _name = 'edition_echeancier.edition_echeancier'
#     _description = 'edition_echeancier.edition_echeancier'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
