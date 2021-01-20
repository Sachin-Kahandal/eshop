from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        verbose_name_plural = 'Catagories'