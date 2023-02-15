import uuid


class UUID:

    @staticmethod
    def generate() -> uuid.UUID:
        return uuid.uuid4()

    @staticmethod
    def validate(uuid_check: str) -> bool:
        try:
            return uuid.UUID(str(uuid_check))
        except ValueError:
            return False

    @staticmethod
    def is_instance(uuid_check: str) -> bool:
        return isinstance(uuid_check, uuid.UUID)
