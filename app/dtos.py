from ast import Str
from dataclasses import dataclass


@dataclass
class FakeIdentity():
    name: str
    second_name: str
    gender: str
    date_of_birth: str
    login: str
    password: str
