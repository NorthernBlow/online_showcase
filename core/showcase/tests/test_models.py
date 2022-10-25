from django.test import TestCase
from showcase.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """
        Test Category model return data name
        :return:
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title="django", slug='django', created_by_id=1,
                                            price='2000', image='', is_active=1, in_stock=1, id=1)

    def test_product_model_entry(self):
        """
        Test Product model data
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django')