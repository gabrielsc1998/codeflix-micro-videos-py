
from abc import ABC
import json
from dataclasses import dataclass, field, fields
from __seedwork.domain.exceptions import InvalidUuidException
from .utils import UUID

# ABC - Abstract Base Class


@dataclass(frozen=True, slots=True)
class ValueObject(ABC):

    def __str__(self) -> str:
        fields_name = [field.name for field in fields(self)]
        return str(getattr(self, fields_name[0])) \
            if len(fields_name) == 1 \
            else json.dumps({field_name: getattr(self, field_name) for field_name in fields_name})


@dataclass(frozen=True, slots=True)
class UniqueEntityId(ValueObject):

    id: str = field(
        default_factory=lambda: str(UUID.generate())
    )

    def __post_init__(self):
        id_value = str(self.id) if UUID.is_instance(self.id) else self.id
        object.__setattr__(self, 'id', id_value)
        self.__validate()

    def __validate(self):
        if UUID.validate(self.id):
            return True
        raise InvalidUuidException()
