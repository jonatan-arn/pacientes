from odoo import models, fields, api


hoy= fields.date.today
mañana = fields.date.today
delta = hoy -mañana
print(delta)