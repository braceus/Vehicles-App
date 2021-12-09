# -*- coding: utf-8 -*-
{
    'name': "/home/brajean/custom_addons/vehicles_app",

    'summary': """
        App que realiza el registro de los servicios y 
        reportes realizados a vehiculos""",

    'description': """
        App de registro de servicios realizados a vehiculos
    """,

    'author': "Brajean Arce Uscachi",


    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir_model_access.xml',
        'reports/templates.xml',
        'reports/report.xml',
        'views/va_vehiculo_views.xml',
        'views/va_service_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
