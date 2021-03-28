from django.db import models


class Folder(models.Model):
    """
    Модель таблицы папок в базе данных.
    """
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Родительская папка')
    name = models.CharField(max_length=255, verbose_name='Название папки')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class File(models.Model):
    """
        Модель таблицы файлов в базе данных.
    """
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE, verbose_name="Папка", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Имя файла", unique=True)
    file = models.FileField(upload_to='uploaded_files', verbose_name="Файл")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
