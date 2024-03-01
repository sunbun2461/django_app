from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=10.99)
        self.product2 = Product.objects.create(name='Product 2', price=19.99)
        self.product3 = Product.objects.create(name='Product 3', price=5.99)

    def test_product_str(self):
        self.assertEqual(str(self.product1), 'Product 1')
        self.assertEqual(str(self.product2), 'Product 2')
        self.assertEqual(str(self.product3), 'Product 3')

    def test_product_query(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        products = response.context['products']
        self.assertEqual(len(products), 3)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)
        self.assertIn(self.product3, products)