#!/usr/bin/env python3
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    def create_session(self, user_id: str = None) -> str:
        session_id = super().create_session(user_id)
        new_user_session = UserSession()
        new_user_session.user_id = user_id
        new_user_session.session_id = session_id
        new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        # user_id = UserSession.search({"session_id": session_id})
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        return super().destroy_session(request)
