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


class Membership(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.name, self.date_joined

