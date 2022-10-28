from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



## категории товаров
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='content/images/%Y%m%d/', blank=True)
    is_published = models.BooleanField(default=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    #вместо QuerySet названия объекта используем метод для строкового представления объекта
    def __str__(self):
        return self.name



## продавцы
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255, db_index=True)
    title = models.CharField(max_length=255, default='Продавец', blank=False)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, default='', blank='false')
    vendor_email = models.EmailField()
    password = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True)
    image = models.ImageField(upload_to='content/vendor_images/%Y%m%d/')


    class Meta:
        verbose_name_plural = 'Магазины'
        verbose_name = 'Магазин'

    def register(self):
        self.save()

    @staticmethod
    def get_all_vendors():
        return Vendor.objects.all()

    @staticmethod
    def get_vendors_by_category(category_id):
        if category_id:
            return Vendor.objects.filter(category=category_id)
        else:
            return Vendor.get_all_vendors()

    def isExists(self):
        if Vendor.objects.filter(vendor_name=self.vendor_name):
            return True
        return False

    def __str__(self):
        return self.title

## карточка товара
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Vendor, on_delete=models.CASCADE, max_length=255, default='admin')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='content/product_images/%Y%m%d/', blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'
        ordering = ('-created_at', )

    #вместо QuerySet названия объекта используем метод для строкового представления объекта
    def __str__(self):
        return self.title




##  ЮЗВЕРИ  ##
class Customer(models.Model):
    nickname = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
        ordering = ('-registration_date', )

    @staticmethod
    def get_customer_by_nick(nick):
        try:
            return Customer.objects.get(nickname=nick)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(nickname=self.nickname):
            return True
        return False

    def __str__(self):
        return self.nickname



## заказанные товары
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    price = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    address = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'
        ordering = ('-date', )