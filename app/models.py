from django.db import models
from smart_selects.db_fields import ChainedManyToManyField
from django.utils.html import format_html
# Create your models here.
class BotUser(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="BotUser name",help_text="Enter name")
    telegram_id = models.CharField(max_length=20,unique=True,verbose_name="Telegram ID",help_text="Enter telegram ID")
    language = models.CharField(max_length=5,default='uz',verbose_name="User language",help_text="Enter user language")
    phone = models.CharField(max_length=20,null=True,blank=True,verbose_name="Phone number",help_text="Ënter user number")
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'BotUser'
        managed = True
        verbose_name = 'BotUser'
        verbose_name_plural = 'BotUsers'
class Category(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="Category",help_text="Enter category name")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class SubCategory(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="SubCategory",help_text="Enter subcategory name")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category",related_name="subcategory")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'SubCategory'
        managed = True
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
class Product(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="SubCategory",help_text="Enter subcategory name")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category",related_name="products")
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,verbose_name="SubCategory",related_name="products")
    # ChainedManyToManyField(
    #     SubCategory,
    #     chained_field="category",
    #     chained_model_field="category",
    #     # show_all=False,
    #     # auto_choose=True,
    #     # sort=True,
    #     related_name = 'products'
    # )
    image = models.ImageField(upload_to='product-images',verbose_name="Image",null=True,blank=True)
    about = models.TextField(null=True,blank=True,verbose_name="Product outline",help_text="Enter brief information about Product")
    price = models.IntegerField(null=True,blank=True,verbose_name="Product price")
    discount = models.IntegerField(null=True,blank=True,verbose_name="Product discount")
    @property
    def pic(self):
        if self.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
        else:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format('https://img.freepik.com/premium-photo/graduation-student-standing-with-diploma_255667-15599.jpg'))

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
class Order(models.Model):
    user = models.ForeignKey(BotUser,on_delete=models.CASCADE,verbose_name="User")
    @property
    def all_shopping(self):
        items = self.items.all()
        # summa = 0 
        # for item in items:
        #     summa += item.shopping
        total = sum([item.shopping for item in items]) 
        return total
    @property
    def all_products(self):
        items = self.items.all()
        total = sum([item.quantity for item in items]) 
        return total
    def __str__(self):
        if self.user.name:
            return self.name
        else:
          return f"User with ID: {self.user.telegram_id}"
    class Meta:
        db_table = 'Order'
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Basket",related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product")
    quantity = models.IntegerField(verbose_name="Product quantity",default=1)
    @property
    def shopping(self):
        if self.product.discount:
            return (self.product.price - self.product.discount) * self.quantity
        else:
            return (self.product.price) * self.quantity
    @property
    def product_id(self):
        return self.product.id
    @property
    def product_name(self):
        return self.product.name
    def __str__(self):
        return self.order
    class Meta:
        db_table = 'OrderItems'
        managed = True
        verbose_name = 'OrderItems'
        verbose_name_plural = 'OrderItems'  