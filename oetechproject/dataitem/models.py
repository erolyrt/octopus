from django.db import models

# Create your models here.

class DataItem(models.Model):
    item_id = models.IntegerField(default=0)
    reference = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    owner = models.CharField(max_length=100)
    #any necessary information field can be added based on CSV file - due to the time limitation, only those parameters were created

    def __str__(self) -> str:
        return f"{self.reference} - {self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)