from django.db import models


class LoanPetition(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    dni = models.CharField(max_length=10)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    ammount = models.DecimalField(max_digits=8, decimal_places=2)  # up to 999,999.99
    approved = models.BooleanField(default=False)
