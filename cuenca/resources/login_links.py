from typing import ClassVar, cast

from pydantic.dataclasses import dataclass

from ..http import Session, session as global_session
from .base import Creatable, Retrievable


@dataclass
class LoginLink(Creatable, Retrievable):
    _resource: ClassVar = 'login_link'
    link: str

    @classmethod
    def create(cls, session: Session = global_session) -> 'LoginLink':
        """
        Use this method to create a link
        :return: Link you can use to log in
        """
        return cast('LoginLink', cls._create(session=session))
