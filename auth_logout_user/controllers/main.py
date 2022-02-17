import werkzeug
import os

import odoo
from odoo.http import Controller, route, request


def clear_session_history(u_sid, f_uid=False):
    """Clear all the user session histories for a particular user"""
    path = odoo.tools.config.session_dir
    store = werkzeug.contrib.sessions.FilesystemSessionStore(
        path, session_class=odoo.http.OpenERPSession, renew_missing=True
    )
    session_fname = store.get_session_filename(u_sid)
    try:
        os.remove(session_fname)
        return True
    except OSError:
        pass
    return False


class AuthLogoutUser(Controller):
    @route(
        "/auth/logout_user/<int:user_id>",
        auth="jwt_auth_logout_user_jwt",
        type="json",
        methods=["POST"],
    )
    def auth_logout_user(self, **kw):
        user = request.env["res.users"].sudo().browse(kw.get("user_id", False))
        # clear user session
        if user:
            session_cleared = clear_session_history(user.sid, kw.get("user_id", False))
            if session_cleared:
                # clear user session
                user._clear_session()
                return True
        return False
