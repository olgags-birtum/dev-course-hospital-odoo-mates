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
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("ongoing", "Ongoing"),
            ("done", "Done"),
            ("canceled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="draft",
    )

    @api.model_create_multi
    # @api.model
    def create(self, vals_list):
        print("odo mates", vals_list)
        for val in vals_list:
            if not val.get("state") or val["state"] == "draft":
                val["state"] = "confirmed"
            if not val.get("reference") or val["reference"] == "New":
                val["reference"] = self.env["ir.sequence"].next_by_code(
                    "hospital.appointment"
                )

        return super(HospitalAppointment, self).create(vals_list)

    def confirm_appointment(self):
        for object in self:
            object["state"] = "confirmed"

    def ongoing_appointment(self):
        for object in self:
            object["state"] = "ongoing"

    def done_appointment(self):
        for object in self:
            object["state"] = "done"

    def cancel_appointment(self):
        for object in self:
            object["state"] = "canceled"
