from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BaseClass):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.title} - {self.author}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(BaseClass):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.book}'
