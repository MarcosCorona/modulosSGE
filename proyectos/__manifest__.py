# -*- coding: utf-8 -*-
{
    'name': "Proyectos empleados",

    'summary': """
        En este modulo podemos asignar a diferentes empleados
        """,

    'description': """
        Este modulo fue desarrollado para gestionar los proyectos
    """,

    'author': "Rafa SaliNipon",
    'website': "http://infsalinas.sytes.net:10445",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/proyectos_security.xml' ,
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/proyecto_idDpto_report.xml',
        'report/proyecto_idProyecto_report.xml',
        #'data/proyectos_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True ,
}
