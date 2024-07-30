from django.db import models

# Create your models here.

'''category_choice = (
    ('Grains', 'Grains'),
    ('Seeds', 'Seeds'),
    ('Consultancy', 'Consultancy')
)'''


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    stock_name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    quantity_purchased = models.IntegerField(default=0, blank=True, null=True)
    purchased_by = models.CharField(max_length=100, blank=True, null=True)
    quantity_sold = models.IntegerField(default=0, blank=True, null=True)
    sold_by = models.CharField(max_length=100, blank=True, null=True)
    sold_to = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(blank=True, null=True)

    date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    export_to_csv = models.BooleanField(default=False)

    def __str__(self):
        return self.stock_name


class StockDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    stock_name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    quantity_purchased = models.IntegerField(default=0, blank=True, null=True)
    purchased_by = models.CharField(max_length=100, blank=True, null=True)
    quantity_sold = models.IntegerField(default=0, blank=True, null=True)
    sold_by = models.CharField(max_length=100, blank=True, null=True)
    sold_to = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
