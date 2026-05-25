# -*- coding: utf-8 -*-
{
    "name": "Localización Politico Territorial Venezolana: Municipios y Parroquias",
    "version": "19.0.0.0.1",
    "author": "Empero LLC",
    "category": "Localization",
    "description":
        """
Localización Venezolana: Municipios y Parroquias
================================================

Basado en información del INE del año 2013, añade los campos de municipio y parroquia en el modelo `res.partner` de
manera que queden disponibles en todos los campos de dirección en modelos derivados como `res.users` o `res.company`.
     """,
    'license': 'LGPL-3',
	'images': ['static/description/icon.png'],
    "depends": ['base', ],
    "data": [
        'security/ir.model.access.csv',
        'data/res.country.state.xml',
        'data/res.country.state.municipality.xml',
        'data/res.country.state.municipality.parish.xml',
        'views/res_company_views.xml',
        'views/l10n_ve_dpt_view.xml',
        'views/res_partner.xml',
    ],
    "installable": True
}
