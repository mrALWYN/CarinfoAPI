from django.db import models

class CarListing(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    features = models.TextField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.name} {self.model}"
