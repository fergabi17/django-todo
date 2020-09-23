from django.test import TestCase
from .models import Items


# Create your tests here.
class TestModels(TestCase):
    def test_done_default_items_false(self):
        item = Items.objects.create(name= 'Test todo item')
        self.assertFalse(item.done)
        
    def test_item_string_method_returns_name(self):
        item = Items.objects.create(name= 'Test todo item')
        self.assertEqual(str(item), 'Test todo item')