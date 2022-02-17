================
Auth Logout User
================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is intended to be in every module    !!
   !! to explain why and how it works.               !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


.. User https://shields.io for badge creation.
.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-PersiscalConsulting%2Fnubox-lightgray.png?logo=github
    :target: https://github.com/PersiscalConsulting/nubox
    :alt: PersiscalConsulting/nubox

|badge1| |badge2| |badge3|

.. !!! Description must be max 2-3 paragraphs, and is required.

This module creates and endpoint to request an user session to expire.

**Table of contents**

.. contents::
   :local:

.. !!! Instalation: must only be present if there are very specific installation instructions, such as installing non-python dependencies.The audience is systems administrators. ] To install this module, you need to: !!!

Usage
=====

1. A new JWT Validator record will be created. Check for auth_logout_user_jwt validator and change the secret key to be used from external conections.
2. Make the API request to https://<base_url>/auth/logout_user/<int:user_id> and the user should be disconnected.

Code example::

    import time
    import json
    import requests
    from jose import jwt

    TOKEN = jwt.encode(
        {
            "aud": "auth_logout_user_jwt",
            "iss": "theissuer",
            "exp": time.time() + 60,
            "email": "admin",
        },
        key="!?#logout_api_secretkey!?#",  # They key is set in Odoo JWT Validators configuration.
        algorithm=jwt.ALGORITHMS.HS256,
    )

    response = requests.post(
        "http://localhost:8069/auth/logout_user/2",  # Set the user id here as parameter.
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json",
        },
        data=json.dumps({}),
    )

    response.raise_for_status()

    print(response.json())

    # User logged out:
    # {'jsonrpc': '2.0', 'id': None, 'result': True}

    # User not logged out:
    # {'jsonrpc': '2.0', 'id': None, 'result': False}


Known issues / Roadmap
======================

* Nothing at the moment.

Bug Tracker
===========

* Contact to the development team

Credits
=======

Authors
~~~~~~~

* Persiscal Consulting S.R.L.

Contributors
~~~~~~~~~~~~

* `Persiscal Consulting S.R.L. <https://www.persiscalconsulting.com/>`_

  * Federico Gregori

Maintainers
~~~~~~~~~~~

This module is maintained by

.. image:: https://i.imgur.com/n9oV9cg.png
   :alt: Persiscal Consulting S.R.L.
   :target: https://www.persiscalconsulting.com/