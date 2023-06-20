# -*- coding: utf-8 -*-
{
    'name': "edition_echeancier",
    'description': """
        edition échéancier
    """,
    'author': "Infotech Consulting Services",
    'website': "https://website.ics-tn.com/",
    'category': 'Uncategorized',
    'version': '13.0.1.3',
    'depends': ['base','account','l10n_tn_check_payment'],
    'data': [
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/edition_report.xml',
        'wizard/popup_view.xml',
        'views/menu.xml',
    ],
}
