from dataclasses import dataclass


@dataclass
class UserData:
    username: str = "new-user"
    password: str = "p@ssw0RD"
