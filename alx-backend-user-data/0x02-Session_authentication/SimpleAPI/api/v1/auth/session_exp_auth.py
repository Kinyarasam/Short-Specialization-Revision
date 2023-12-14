#!/usr/bin/env python3
from .session_auth import SessionAuth
import os
import datetime


class SessionExpAuth(SessionAuth):
    def __init__(self) -> None:
        super().__init__()
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id: str = None) -> str:
        session_id = super().create_session(user_id)
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        if session_id is None:
            return None
        user_details = self.user_id_by_session_id.get(session_id)
        if user_details is None:
            return None
        if "created_at" not in user_details.keys():
            return None
        if self.session_duration <= 0:
            return user_details.get("user_id")
        created_at = user_details.get("created_at")
        allowed_window = created_at + \
            datetime.timedelta(seconds=self.session_duration)
        if allowed_window < datetime.datetime.now():
            return None
        return user_details.get("user_id")
