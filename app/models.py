from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = "カテゴリ名"
        verbose_name_plural = "カテゴリ名"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Author(models.Model):
    class Meta:
        verbose_name = "著者名"
        verbose_name_plural = "著者名"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        verbose_name = "書籍"
        verbose_name_plural = "書籍"

    name = models.CharField(verbose_name="書籍名",max_length=255)
    author = models.ForeignKey(Author,verbose_name="著者名",on_delete = models.CASCADE ,blank=True, null=True)
    categories = models.ManyToManyField(Category,verbose_name="カテゴリ名",  blank=True)

    def __str__(self):
        return self.name
