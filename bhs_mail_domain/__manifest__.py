# -*- encoding: utf-8 -*-
{
    'name': "Mail Domain",
    'version': '1.0',
    'summary': 'BHS Mail',
    'category': 'Mail',
    'description': """BH Mail""",
    "depends": ['mail', 'base_setup'],
    'data': [
        'views/mail_res_config_settings.xml'
    ],
    # Author
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
