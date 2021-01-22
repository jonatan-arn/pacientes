# -*- coding: utf-8 -*-

from odoo import models, fields, api


class historial_model(models.Model):
    _name = 'pacientes.historial_model'
    _description = 'modulo de Historiales'

    name = fields.Char(string="Cita",index=True,required=True)
    fecha = fields.Date(string="Fecha cita",index=True,required=True,default=fields.Date.today)
    paciente_id = fields.Many2one("pacientes.paciente_model")