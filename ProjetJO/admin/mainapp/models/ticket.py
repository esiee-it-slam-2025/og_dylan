from django.db import models
from django.contrib.auth.models import User
import uuid

class Ticket(models.Model):
    CATEGORIES = [
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('PLATINUM', 'Platinum'),
    ]

    PRICES = {
        'SILVER': 100,
        'GOLD': 200,
        'PLATINUM': 300,
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='tickets')
    category = models.CharField(max_length=10, choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    seat = models.CharField(max_length=10, null=True, blank=True)
    is_used = models.BooleanField(default=False)  # Nouveau champ pour suivre l'utilisation du ticket

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.PRICES[self.category]
        if not self.seat:
            self.seat = self._generate_seat_number()
        super().save(*args, **kwargs)

    def _generate_seat_number(self):
        prefix = self.category[0] 
        taken_seats = Ticket.objects.filter(
            event=self.event,
            category=self.category
        ).values_list('seat', flat=True)
        
        number = 1
        while True:
            seat_num = f"{prefix}-{str(number).zfill(2)}"
            if seat_num not in taken_seats:
                return seat_num
            number += 1

    def __str__(self):
        return f"Ticket {self.id} - {self.event} - {self.category} - Place {self.seat}"