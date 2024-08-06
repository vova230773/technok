from django.db import models

class product_mod(models.Model):
    guid = models.CharField(max_length=99,unique=True, verbose_name='guid')
    create_at = models.DateTimeField(blank=True,auto_now_add=True, verbose_name='Дата створення')
    # product=models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='ТМЦ')
    name = models.CharField(max_length=500,unique=True, verbose_name='Найменування')

    class Meta:
        db_table = 'product'
        verbose_name = 'ТМЦ'
        verbose_name_plural = 'ТМЦ'# Create your models here.

    def __str__(self):
        return self.name