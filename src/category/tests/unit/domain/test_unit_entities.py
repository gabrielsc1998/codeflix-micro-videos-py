# pylint: disable=unexpected-keyword-arg
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime
import unittest
from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(name='Movie')
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

        created_at = datetime.now()
        category = Category(
            name='Movie',
            description='some description',
            is_active=False,
            created_at=created_at
        )

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, False)
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name='Movie 1')
        category2 = Category(name='Movie 2')
        # Esta forma também funciona
        # self.assertNotEqual(
        #     category1.created_at,
        #     category2.created_at
        # )
        self.assertNotEqual(
            category1.created_at.timestamp(),
            category2.created_at.timestamp()
        )

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Category(name='test')
            value_object.name = 'fake id'

    def test_update_category(self):
        category = Category(name='test')
        self.assertEqual(category.name, 'test')
        self.assertIsNone(category.description)
        category.update('new name', 'this is a category')
        self.assertEqual(category.name, 'new name')
        self.assertEqual(category.description, 'this is a category')

    def test_activate_category(self):
        category = Category(name='test', is_active=False)
        self.assertFalse(category.is_active)
        category.activate()
        self.assertTrue(category.is_active)

    def test_deactivate_category(self):
        category = Category(name='test', is_active=True)
        self.assertTrue(category.is_active)
        category.deactivate()
        self.assertFalse(category.is_active)
