# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /opt/odoo/custom-addons/pacientes(models.Model):
#     _name = '/opt/odoo/custom-addons/pacientes./opt/odoo/custom-addons/pacientes'
#     _description = '/opt/odoo/custom-addons/pacientes./opt/odoo/custom-addons/pacientes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
