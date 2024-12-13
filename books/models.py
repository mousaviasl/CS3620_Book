from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)  # Allow blank or null images

    def __str__(self):
        return self.name
