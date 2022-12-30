from django.db import models
from rental.models import Rental


class Reservation(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE, )

    def get_info(self):
        return f"|{Rental.get_name(self.rental_id)}   |{self.id}| {self.checkin}|{self.checkout}| prev-res"

    def get_id(self):
        return str(self.id)