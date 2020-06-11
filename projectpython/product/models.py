from django.db import models


# Create your models here.

class ProductManager(models.Manager):

    def validator(self, postData):
        errors = {}
        if (postData['product_name'].isalpha()) == False:
            if len(postData['product_name']) < 2:
                errors['product_name'] = "Product name can not be shorter than 2 characters"

        if (postData['product_weight'].isalpha()) == False:
            if len(postData['product_weight']) < 2:
                errors['product_weight'] = "product_weight can not be shorter than 2 characters"

        if len(postData['product_price']) == 0:
            errors['product_price'] = "You must enter an price"

        return errors


class Product(models.Model):

    product_name = models.CharField(max_length=255)
    product_weight = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    class Meta:
        app_label = 'product'


class ProductRouter(object):
    """
    A router to control app1 db operations
    """

    def db_for_read(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'productdb' not in settings.DATABASES:
            return None

        if model._meta.app_label == 'product':
            return 'productdb'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'productdb' not in settings.DATABASES:
            return None

        if model._meta.app_label == 'product':
            return 'productdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in app1 is involved"
        from django.conf import settings
        if 'productdb' not in settings.DATABASES:
            return None

        if obj1._meta.app_label == 'product' or obj2._meta.app_label == 'product':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the app1 app only appears on the 'app1' db"
        from django.conf import settings
        if 'productdb' not in settings.DATABASES:
            return None

        if db == 'productdb':
            return model._meta.app_label == 'product'
        elif model._meta.app_label == 'product':
            return False
        return None
