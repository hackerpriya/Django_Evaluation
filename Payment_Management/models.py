from django.db import models
class ServiceUser(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class Services(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('Mobile Recharge', 'Mobile Recharge'),
        ('DTH Recharge', 'DTH Recharge'),
        ('Insurance Payment', 'Insurance Payment'),
    ]

    MODE_OF_PAYMENT_CHOICES = [
        ('UPI', 'UPI'),
        ('Internet Banking', 'Internet Banking'),
        ('Card Payment', 'Card Payment'),
    ]

    type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    mode_of_payment = models.CharField(max_length=50, choices=MODE_OF_PAYMENT_CHOICES)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.type} - {self.company}"

class Subscription(models.Model):
    service_user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_user} - {self.service} - {self.amount}"


