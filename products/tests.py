from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Category, Product
from cart.cart import Cart


class ProductsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        self.product = Product.objects.create(
            name='Test Coffee',
            slug='test-coffee',
            category=self.category,
            description='Test description',
            price=25000,
            available=True,
            stock=10
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_product_detail_view(self):
        response = self.client.get(
            reverse('products:product_detail', args=[self.product.id, self.product.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_category_view(self):
        response = self.client.get(
            reverse('products:product_list_by_category', args=[self.category.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)


class CartTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        self.product = Product.objects.create(
            name='Test Coffee',
            slug='test-coffee',
            category=self.category,
            description='Test description',
            price=25000,
            available=True,
            stock=10
        )

    def test_cart_add(self):
        response = self.client.post(
            reverse('cart:cart_add', args=[self.product.id]),
            {'quantity': 2, 'override': False}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after adding

    def test_cart_detail(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)


class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login_view(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
