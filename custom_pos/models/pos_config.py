from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    disable_discount = fields.Boolean(string='Disable Discount')
    disable_price = fields.Boolean(string='Disable Price')
    send_auto_email = fields.Boolean(string="Auto Send")
