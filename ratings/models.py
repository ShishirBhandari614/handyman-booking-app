from django.db import models

# Create your models here.
class Booking(models.Model):
    customer = models.ForeignKey("userauth.Customer", on_delete=models.CASCADE)
    service_provider = models.ForeignKey("userauth.ServiceProvider", on_delete=models.CASCADE)
    service_type = models.CharField(max_length=255)
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])
    # Other booking-related fields...
    
    def __str__(self):
        return f"Booking {self.id} for {self.customer.username}"

class Rating(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    review = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for Booking {self.booking.id}"

class Cancellation(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    reason = models.TextField()
    date_canceled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cancellation for Booking {self.booking.id}"
