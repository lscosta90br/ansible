from django.db import models
from django.utils import timezone


class exemploxpto(models.Model):
    descricao = models.CharField('descricao', max_length=20)
    observacao = models.TextField('observação', blank=True)
    data_publicacao = models.DateTimeField(default=timezone.now)


    class Meta:
        db_table = "tbl_exemplo"
        verbose_name = 'exemploxpto'
        verbose_name_plural = 'exemplosxpto'