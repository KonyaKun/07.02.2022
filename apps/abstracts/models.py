from django.db import models

# Create your models here.

class AbstractDateTime(models.Model):
    datetime_created = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add=True
        )
    datetime_updated = models.DateTimeField(
        verbose_name='время обновления',
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name='время удаления',
        null=True,
        blank=True
    )
    class Meta:
        abstract=True

    def __str__(self) -> str:
        return f'Время создания - {self.date_created} \
            Дата изменения - {self.date_updated} \
            Дата удаления - {self.date_deleted}'