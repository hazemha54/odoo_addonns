from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class edition_wiz(models.TransientModel):

    _name = 'edition.wizard'

    date_from = fields.Date(string="De", )
    date_to = fields.Date(string="Jusqu'a", )
    grouped = fields.Boolean(string="Grouper", default=False)

    supplier = fields.Many2one('res.partner',string="Fournisseur" , domain=[('supplier_rank','>=', 1)])

    customer = fields.Many2one('res.partner',string="Client", domain=[('customer_rank','>=', 1)])

    def print_report(self):
        vals = []
        vals1 = []
        vals2 = []
        vals3 = []
        vals4 = []
        vals5 = []
        vals6 = []
        vals7 = []
        vals8 = []
        vals9 = []
        vals10 = []
        vals11 = []
        vals12 = []
        total1 = 0
        total2 = 0
        total3 = 0
        total4 = 0
        total5 = 0
        total6 = 0
        total7 = 0
        total8 = 0
        total9 = 0
        total10 = 0
        total11= 0
        total12 = 0
        if (self.supplier.id not in ['',"",None,False]) and (self.customer.id in ['',"",None,False]) :
            if (self.date_to not in ['', "", None, False]) and (self.date_from not in ['', "", None, False]):
                reports = self.env["account.treasury"].sudo().search(
                    [('clearing_date', '>=', self.date_from), ('clearing_date', '<=', self.date_to),
                     ('partner_id.id', '=', self.supplier.id)], [], order='clearing_date')

            elif (self.date_to in ['', "", None, False]) and (self.date_from in ['', "", None, False]):
                reports = self.env["account.treasury"].sudo().search(
                    [('partner_id.id', '=', self.supplier.id)], [],
                    order='clearing_date')
            elif (self.date_to in ['', "", None, False]) and (self.date_from not in ['', "", None, False]):
                raise ValidationError('Please select date')
            elif (self.date_to not in ['',"",None,False]) and (self.date_from in ['',"",None,False]) :
                raise ValidationError('Please select date')
            if self.grouped == False:
                for rec in reports:
                    print ('rec.type_transaction',rec.type_transaction)
                    vals.append({
                        'months': rec.clearing_date.strftime('%m'),
                        'date': rec.clearing_date,
                        'name': rec.name,
                        'partenr_id': rec.partner_id,
                        'state': rec.state,
                        'amount': rec.amount,
                        'partner_id': rec.partner_id.name,
                        'type_transaction': rec.type_transaction,
                    })
                data = {
                    'ids': self.ids,
                    'model': self._name,
                    'vals': vals,
                    'date_from': self.date_from,
                    'date_to': self.date_to,
                }
                return self.env.ref('edition_echeancier.report_payment_54').report_action(self, data=data)
            else:
                for rec in reports:
                    print ('rec.type_transaction',rec.type_transaction)
                    if rec.clearing_date.strftime('%m') == '01':
                        total1 = total1 + rec.amount
                        vals1.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '02':
                        total2 = total2 + rec.amount
                        vals2.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '03':
                        total3 = total3 + rec.amount
                        vals3.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '04':
                        total4 = total4 + rec.amount
                        vals4.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '05':
                        total5 = total5 + rec.amount
                        vals5.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '06':
                        total6 = total6 + rec.amount
                        vals6.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '07':
                        total7 = total7 + rec.amount
                        vals7.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '08':
                        total8 = total8 + rec.amount
                        vals8.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '09':
                        total9 = total9 + rec.amount
                        vals9.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '10':
                        total10 = total10 + rec.amount
                        vals10.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '11':
                        total11 = total11 + rec.amount
                        vals11.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '12':
                        total12 = total12 + rec.amount
                        vals12.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                data = {
                    'grouped': self.grouped,
                    'ids': self.ids,
                    'model': self._name,
                    'vals1': vals1,
                    'vals2': vals2,
                    'vals12': vals12,
                    'vals3': vals3,
                    'vals4': vals4,
                    'vals5': vals5,
                    'vals6': vals6,
                    'vals7': vals7,
                    'vals8': vals8,
                    'vals9': vals9,
                    'vals10': vals10,
                    'vals11': vals11,
                    'date_from': self.date_from,
                    'date_to': self.date_to,
                    'total1': total1,
                    'total2': total2,
                    'total3': total3,
                    'total4': total4,
                    'total5': total5,
                    'total6': total6,
                    'total7': total7,
                    'total8': total8,
                    'total9': total9,
                    'total10': total10,
                    'total11': total11,
                    'total12': total12,
                }
                return self.env.ref('edition_echeancier.report_payment_54').report_action(self, data=data)

        elif (self.supplier.id in ['',"",None,False]) and (self.customer.id not in ['',"",None,False]) :
            if (self.date_to not in ['',"",None,False]) and (self.date_from not in ['',"",None,False]) :
                reports = self.env["account.treasury"].sudo().search(
                    [('clearing_date', '>=', self.date_from), ('clearing_date', '<=', self.date_to),('partner_id.id', '=', self.customer.id)], [],order='clearing_date')

            elif (self.date_to in ['', "", None, False]) and (self.date_from in ['', "", None, False]):
                reports = self.env["account.treasury"].sudo().search(
                    [('partner_id.id', '=', self.customer.id),], [],order='clearing_date')
            elif (self.date_to in ['',"",None,False]) and (self.date_from not in ['',"",None,False]) :
                raise ValidationError('Please select date')
            elif (self.date_to not in ['',"",None,False]) and (self.date_from in ['',"",None,False]) :
                raise ValidationError('Please select date')
            if self.grouped == False :
                for rec in reports:
                    vals.append({
                        'months': rec.clearing_date.strftime('%m'),
                        'date': rec.clearing_date,
                        'name': rec.name,
                        'partenr_id': rec.partner_id,
                        'state': rec.state,
                        'amount': rec.amount,
                        'partner_id': rec.partner_id.name,
                        'type_transaction': rec.type_transaction,
                    })
                data = {
                    'title': 'Edition Échéancier Reglements Client',
                    'ids': self.ids,
                    'model': self._name,
                    'vals': vals,
                    'date_from': self.date_from,
                    'date_to': self.date_to,
                }
                return self.env.ref('edition_echeancier.report_payment_54').report_action(self, data=data)
            else:
                for rec in reports :
                    print('rec.type_transaction', rec.type_transaction)
                    if rec.clearing_date.strftime('%m') == '01' :
                        total1 = total1 + rec.amount
                        vals1.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '02':
                        total2 = total2 + rec.amount
                        vals2.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '03':
                        total3 = total3 + rec.amount
                        vals3.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '04':
                        total4 = total4 + rec.amount
                        vals4.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '05':
                        total5 = total5 + rec.amount
                        vals5.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '06':
                        total6 = total6 + rec.amount
                        vals6.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '07':
                        total7 = total7 + rec.amount
                        vals7.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '08':
                        total8 = total8 + rec.amount
                        vals8.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '09':
                        total9 = total9 + rec.amount
                        vals9.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '10':
                        total10 = total10 + rec.amount
                        vals10.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '11':
                        total11 = total11 + rec.amount
                        vals11.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                    if rec.clearing_date.strftime('%m') == '12':
                        total12 = total12 + rec.amount
                        vals12.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                data = {
                    'grouped':self.grouped,
                    'ids': self.ids,
                    'model': self._name,
                    'vals1': vals1,
                    'vals2': vals2,
                    'vals12': vals12,
                    'vals3': vals3,
                    'vals4': vals4,
                    'vals5': vals5,
                    'vals6': vals6,
                    'vals7': vals7,
                    'vals8': vals8,
                    'vals9': vals9,
                    'vals10': vals10,
                    'vals11': vals11,
                    'date_from': self.date_from,
                    'date_to': self.date_to,
                    'total1': total1,
                    'total2': total2,
                    'total3': total3,
                    'total4': total4,
                    'total5': total5,
                    'total6': total6,
                    'total7': total7,
                    'total8': total8,
                    'total9': total9,
                    'total10': total10,
                    'total11': total11,
                    'total12': total12,
                }
                return self.env.ref('edition_echeancier.report_payment_54').report_action(self, data=data)
        else:
            if (self.date_to not in ['', "", None, False]) and (self.date_from not in ['', "", None, False]):
                reports = self.env["account.treasury"].sudo().search(
                    [('clearing_date', '>=', self.date_from), ('clearing_date', '<=', self.date_to)], [], order='clearing_date')

            elif (self.date_to in ['', "", None, False]) and (self.date_from in ['', "", None, False]):
                reports = self.env["account.treasury"].sudo().search(
                    [], [],order='clearing_date')
            elif (self.date_to in ['', "", None, False]) and (self.date_from not in ['', "", None, False]):
                raise ValidationError('Please select date')
            elif (self.date_to not in ['', "", None, False]) and (self.date_from in ['', "", None, False]):
                raise ValidationError('Please select date')
            if self.grouped == False:
                for rec in reports:
                    vals.append({
                        'months': rec.clearing_date.strftime('%m'),
                        'date': rec.clearing_date,
                        'name': rec.name,
                        'partenr_id': rec.partner_id,
                        'state': rec.state,
                        'amount': rec.amount,
                        'partner_id': rec.partner_id.name,
                        'type_transaction': rec.type_transaction,
                    })

                data = {
                    'title':"Edition Échéancier Reglements",
                    'ids': self.ids,
                    'model': self._name,
                    'vals': vals,
                    'date_from': self.date_from,
                    'date_to': self.date_to,
                }
                return self.env.ref('edition_echeancier.report_payment_54').report_action(self, data=data)
            else:
                for rec in reports:
                    print(rec.type_transaction)
                    if rec.clearing_date.strftime('%m') == '01':
                        total1 = total1 + rec.amount
                        vals1.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '02':
                        total2 = total2 + rec.amount
                        vals2.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '03':
                        total3 = total3 + rec.amount
                        vals3.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '04':
                        total4 = total4 + rec.amount
                        vals4.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '05':
                        total5 = total5 + rec.amount
                        vals5.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '06':
                        total6 = total6 + rec.amount
                        vals6.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '07':
                        total7 = total7 + rec.amount
                        vals7.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '08':
                        total8 = total8 + rec.amount
                        vals8.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '09':
                        total9 = total9 + rec.amount
                        vals9.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '10':
                        total10 = total10 + rec.amount
                        vals10.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '11':
                        total11 = total11 + rec.amount
                        vals11.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })
                    if rec.clearing_date.strftime('%m') == '12':
                        total12 = total12 + rec.amount
                        vals12.append({
                            'months': rec.clearing_date.strftime('%m'),
                            'date': rec.clearing_date,
                            'name': rec.name,
                            'partenr_id': rec.partner_id,
                            'state': rec.state,
                            'amount': rec.amount,
                            'partner_id': rec.partner_id.name,
                            'type_transaction': rec.type_transaction,
                        })

                data = {
                    'grouped': self.grouped,
                    'ids': self.ids,
                    'model': self._name,
                    'vals1': vals1,
                    'vals2': vals2,
                    'vals12': vals12,
                    'vals3': vals3,
                    'vals4': vals4,
                    'vals5': vals5,
                    'vals6': vals6,
                    'vals7': vals7,
                    'vals8': vals8,
                    'vals9': vals9,
                    'vals10': vals10,
                    'vals11': vals11,
                    'date_from': self.date_from,
                    'date_to': self.date_to,
                    'total1': total1,
                    'total2': total2,
                    'total3': total3,
                    'total4': total4,
                    'total5': total5,
                    'total6': total6,
                    'total7': total7,
                    'total8': total8,
                    'total9': total9,
                    'total10': total10,
                    'total11': total11,
                    'total12': total12,
                }
                return self.env.ref('edition_echeancier.report_payment_54').report_action(self, data=data)