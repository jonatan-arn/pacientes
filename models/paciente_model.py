# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime,re
from odoo.exceptions import ValidationError

class paciete_model(models.Model):
    _name = 'pacientes.paciente_model'
    _description = 'modulo de pacientes'

    name = fields.Char(string="Nombre",index=True,required=True)
    apellidos = fields.Char(string="Apellidos",index=True,required=True)
    dni = fields.Char(string="Dni",index=True,required=True)
    telefono = fields.Integer(string="Telefono",index=True,required=True)
    email = fields.Char(string="correo electronico",index=True,required=True)
    nacimiento = fields.Date(string="Fecha de nacimiento",index=True,required=True)
    numero_visitas = fields.Integer(string="Numero de visitas",index=True,required=True, default=0,editable=False)
    historials_visitas = fields.One2many("pacientes.historial_model","paciente_id")
    

    
    @api.constrains('nacimiento')
    def validate_edad(self):
        if not self.comprovar_edad():
            raise ValidationError("Tiene que ser major de edad")


    @api.constrains('email')
    def validate_email(self):
        if not self.comprovar_email(self.email):
            raise ValidationError("Error al introducir en el email")

    def setNumero_visitas(self):
        self.numero_visitas=len(self.historials_visitas)
    
    @api.constrains('dni')
    def validate_dni(self):
        if not self.comprovar_dni(self.dni):
            raise ValidationError("Error al introducir el dni")
        



    def comprovar_edad(self):
        today_date = datetime.date.today()
        edad = fields.Datetime.to_datetime(self.nacimiento).date()
        total_age = int((today_date - edad).days /365)
        if(total_age>=18):
            return True
        else:
            return False


    def comprovar_email(self,email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return True
        
        return False
    def comprovar_dni(self,nif):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dni = nif[:8]
            if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                if tabla[int(dni)%23] == letraControl:
                    return True
        return False               