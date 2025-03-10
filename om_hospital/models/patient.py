# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Master"
    _inherit = ["mail.thread"]
    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth", tracking=True)
    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
        tracking=True,
    )
