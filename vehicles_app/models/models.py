from odoo import models, fields, api


class Vehiculo(models.Model):
    _name = "va.vehiculo"
    _description = "Vehiculo"

    license_plate = fields.Char("Placa")
    owner = fields.Char("Propietario del Vehiculo")
    services_ids = fields.One2many("va.service.lines", "vehicle_id")
    #service_id =

class Servicio(models.Model):
    _name = "va.service"
    _description = "Servicios"

    name = fields.Char("Nombre")
    amount = fields.Float("Monto")
    currency_id = fields.Many2one("res.currency", default=162)

    #vehicle_id = fields.Many2one("va.vehiculo", "Vehiculo")

class ServicioLines(models.Model):
    _name = "va.service.lines"
    _description = "Lineas de Servicio"

    service_id = fields.Many2one("va.service", "Servicio")
    vehicle_id = fields.Many2one("va.vehiculo", "Vehiculo")


