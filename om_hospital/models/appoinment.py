# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment Master"
    _inherit = ["mail.thread"]
    _rec_name = "patient_id"
    reference = fields.Char(
        string="Reference",
        default="New",
        readonly=True,
    )
    patient_id = fields.Many2one("hospital.patient", string="Patient")

    date_of_appointment = fields.Date(string="Date Of Appointment")
    note = fields.Text(
        string="Note",
    )

    
    # @api.model_create_multi
    @api.model
    def create(self, vals_list):
        print("odo mates",vals_list)
        for val in vals_list:
            if not val.get("reference") or val["reference"]=="New":
               val["reference"]=self.env["ir.sequence"].next_by_code("hospital.appointment")

        return super().create(vals_list)
