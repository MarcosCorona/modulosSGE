# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class horarios(models.Model):
#     _name = 'horarios.horarios'
#     _description = 'horarios.horarios'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
#import datetime
from datetime import datetime
from odoo import models, fields, api, exceptions
from dateutil.relativedelta import *
from datetime import date

class bajas(models.Model):
    _name = 'horarios.bajas'
    _description = 'Define los atributos de una baja'

    motivoBaja = fields.Selection(string='Motivo de la baja', selection=[('a','Enfermedad'),('b','Maternidad'),
                                                                         ('c','Paternidad'),('d','Accidente')], required=True)
    gravedadBaja = fields.Selection(string='Gravedad de la baja', selection=[('a','Alta'),('b','Media'),('c','Baja')])

    decripcionBaja = fields.Text(string='Descripción de la baja', required=True, help='Escribe una descripción detallada')
    fechaBaja = fields.Date(string='Fecha de la baja', required=True, default=fields.Date.today())

    #Relacion entre tablas
    empleado_id = fields.Many2one('proyectos.empleado', string='Empleado')

class horario(models.Model):
    _name = 'horarios.horario'
    _description = 'Define los atributos de un horario'

    # Relacion entre tablas
    empleado_id = fields.One2many('proyectos.empleado', 'horario_id')

    # Atributos
    nombreHorario = fields.Char(string='Nombre horario', required=True)

    lunesEntrada = fields.Selection(string='Hora entrada lunes', selection='_get_valid_hours', default='8.5')
    lunesSalida = fields.Selection(string='Hora salida lunes', selection='_get_valid_hours', default='8.5')
    martesEntrada = fields.Selection(string='Hora entrada martes', selection='_get_valid_hours', default='8.5')
    martesSalida = fields.Selection(string='Hora salida martes', selection='_get_valid_hours', default='8.5')
    miercolesEntrada = fields.Selection(string='Hora entra miercoles', selection='_get_valid_hours', default='8.5')
    miercolesSalida = fields.Selection(string='Hora salida miercoles', selection='_get_valid_hours', default='8.5')
    juevesEntrada = fields.Selection(string='Hora entrada jueves', selection='_get_valid_hours', default='8.5')
    juevesSalida = fields.Selection(string='Hora salida jueves', selection='_get_valid_hours', default='8.5')
    viernesEntrada = fields.Selection(string='Hora entrada viernes', selection='_get_valid_hours', default='8.5')
    viernesSalida = fields.Selection(string='Hora salida viernes', selection='_get_valid_hours', default='8.5')

    def name_get(self):
        resultados = []
        for horario in self:
            resultados.append((horario.id, horario.nombreHorario))
        return resultados

    @api.model
    def _get_valid_hours(self):
        selection = [
            ('8', '8:00'), ('8.5', '8:30'),
            ('9', '9:00'), ('9.5', '9:30'),
            ('10', '10:00'), ('10.5', '10:30'),
            ('11', '11:00'), ('11.5', '11:30'),
            ('12', '12:00'), ('12.5', '12:30'),
            ('13', '13:00'), ('13.5', '13:30'),
            ('14', '14:00'), ('14.5', '14:30'),
            ('15', '15:00'), ('15.5', '15:30'),
            ('16', '16:00'), ('16.5', '16:30'),
            ('17', '17:00'), ('17.5', '17:30'),
            ('18', '18:00')
        ]
        return selection

    @api.constrains('lunesEntrada','martesEntrada','miercolesEntrada','juevesEntrada','viernesEntrada')
    def change_data_field(self):
        he = float(self.lunesEntrada)
        hs = float(self.lunesSalida)
        if(he > hs):
            raise exceptions.ValidationError("La hora de salida del lunes tiene que ser mayor que la de entrada")

        he = float(self.martesEntrada)
        hs = float(self.martesSalida)
        if(he > hs):
            raise exceptions.ValidationError("La hora de salida del martes tiene que ser mayor que la de entrada")

        he = float(self.miercolesEntrada)
        hs = float(self.miercolesSalida)
        if (he > hs):
            raise exceptions.ValidationError("La hora de salida del miercoles tiene que ser mayor que la de entrada")

        he = float(self.juevesEntrada)
        hs = float(self.juevesSalida)
        if (he > hs):
            raise exceptions.ValidationError("La hora de salida del jueves tiene que ser mayor que la de entrada")

        he = float(self.viernesEntrada)
        hs = float(self.viernesSalida)
        if (he > hs):
            raise exceptions.ValidationError("La hora de salida del viernes tiene que ser mayor que la de entrada")