# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo/custom-addons/pacientes(http.Controller):
#     @http.route('//opt/odoo/custom-addons/pacientes//opt/odoo/custom-addons/pacientes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/custom-addons/pacientes//opt/odoo/custom-addons/pacientes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/custom-addons/pacientes.listing', {
#             'root': '//opt/odoo/custom-addons/pacientes//opt/odoo/custom-addons/pacientes',
#             'objects': http.request.env['/opt/odoo/custom-addons/pacientes./opt/odoo/custom-addons/pacientes'].search([]),
#         })

#     @http.route('//opt/odoo/custom-addons/pacientes//opt/odoo/custom-addons/pacientes/objects/<model("/opt/odoo/custom-addons/pacientes./opt/odoo/custom-addons/pacientes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/custom-addons/pacientes.object', {
#             'object': obj
#         })
