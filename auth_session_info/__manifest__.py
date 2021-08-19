{
    'name': 'Add session_id to /web/session/authenticate response',
    'author': 'FedericoGregori',
    'depends': ['web'],
    'version': '13.0.1.1',
    'description': """
        Odoo JSON-RPC Authentication (/web/session/authenticate) missing "session_id" parameter added for JSON-RPC API easy access. It was removed in Odoo 13.0 to rely in the use of cookies.
    """,
    'category': 'Technical',
    'sequence': 5,
    'application': False,
    'installable': True,
}
