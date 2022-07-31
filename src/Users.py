from dataclasses import dataclass, field
from dataclasses import astuple, asdict


@dataclass
class Users:
    age: int
    name: str
    gender: str
    address: str


def __eq__(self, other):
    if other.__class__ is not self.__class__:
        return NotImplemented
    return (self.age,
            self.name,
            self.gender,
            self.address) == (other.age,
                              other.name,
                              other.gender,
                              other.address)
