# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Master"
    name = fields.Char(string="Name", required=True)
    dete_of_birth = fields.Date(string="Date Of Birth")
    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
    )
