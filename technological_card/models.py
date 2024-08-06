from django.db import models
from product.models import product_mod
from operation.models import oper_mod

class tk_mod(models.Model):
    guid = models.CharField(max_length=99,unique=True, verbose_name='guid')
    create_at = models.DateTimeField(blank=True,auto_now_add=True, verbose_name='Дата створення')
    product=models.ForeignKey(product_mod, on_delete=models.PROTECT, verbose_name='ТМЦ')
    operation=models.ForeignKey(oper_mod, on_delete=models.PROTECT, verbose_name='Операції')

    class Meta:
        db_table = 'technological_card'
        verbose_name = 'Технологічні карти'
        verbose_name_plural = 'Технологічні карти'
