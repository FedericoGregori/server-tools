# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Auth Logout User",
    "summary": """
        This module creates and endpoint to request an user session to expire.
    """,
    "author": "Persiscal Consulting S.R.L.",
    "maintainers": ["FedericoGregori"],
    "website": "https://www.persiscalconsulting.com/",
    "license": "AGPL-3",
    "category": "Tools",
    "version": "13.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["base", "auth_jwt", "auth_login_user"],
    "data": [
        "data/auth_jwt_validator.xml",
    ],
}
