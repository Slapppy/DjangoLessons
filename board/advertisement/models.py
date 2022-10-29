from django.db import models


# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    @property
    def full_info(self):
        "Returns the person's full name."
        return '%s %s' % (self.name, self.instrument, self.email)


class CalcHistory(models.Model):
    val1 = models.CharField(max_length=50)
    val2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=100, null=True ,blank=True)
    operator = models.CharField(max_length=100)

