from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    disable_discount = fields.Boolean(
        string='Control Discount',
        related="pos_config_id.disable_discount",
        readonly=False
    )
    disable_price = fields.Boolean(
        string='Control Price',
        related="pos_config_id.disable_price",
        readonly=False,
    )
    send_auto_email = fields.Boolean(
        string="Auto Send",
        related="pos_config_id.send_auto_email",
        readonly=False
    )
