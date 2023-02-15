
import unittest
import uuid

from __seedwork.domain.utils import UUID


class TestUUIDUtilstUnit(unittest.TestCase):

    def test_if_generate_an_correct_uuid(self):
        uuid_generated = UUID.generate()
        self.assertTrue(uuid.UUID(str(uuid_generated)))
        self.assertEqual(type(uuid_generated), uuid.UUID)
        self.assertEqual(len(str(uuid_generated)), 36)

    def test_uuid_validate(self):
        uuid_generated = UUID.generate()
        self.assertTrue(UUID.validate(uuid_generated))
        self.assertFalse(UUID.validate('invalid-uuid'))
        self.assertFalse(UUID.validate(123456))

    def test_if_id_is_an_instance_of_uuid(self):
        uuid_generated = UUID.generate()
        self.assertTrue(UUID.is_instance(uuid_generated))
        self.assertFalse(UUID.is_instance(
            'f197f99c-9b1a-485e-a6e4-93bb17beb64e'))
