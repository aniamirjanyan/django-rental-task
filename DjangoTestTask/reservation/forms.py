from django.forms import ModelForm
from reservation.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['checkin', 'checkout', 'rental_id']
