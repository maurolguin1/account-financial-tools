# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class AccountAccountType(models.Model):
    _inherit = 'account.account.type'

    name = fields.Char(translate=False)


class AccountTaxCode(models.Model):
    _inherit = 'account.tax.code'

    name = fields.Char(translate=False)


class AccountTax(models.Model):
    _inherit = 'account.tax'

    name = fields.Char(translate=False)


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    name = fields.Char(translate=False)
    note = fields.Char(translate=False)
