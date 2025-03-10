{
    "name": "Hospital Management System",
    "version": "1.0",
    "description": "Hospital Management System from Odoo mates youtube",
    "website": "hospital.com",
    "depends": [
        'mail',
    ],
    "data": [
         "data/sequence.xml",
        "views/patient_views.xml",
        "views/patient_views_readonly.xml",
       "views/appointment_views.xml",
     
        "views/menu.xml",
        "security/ir.model.access.csv",
    ],
    "license": "LGPL-3",
    "assets": {},
}
