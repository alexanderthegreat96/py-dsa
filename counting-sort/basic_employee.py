from dataclasses import dataclass


@dataclass
class BasicEmployee:
    """ Class storing (very) basic employee details."""
    first_name: str
    last_name: str
    id: int

    def __str__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}'

