from reservation.models import Reservation
from django.http import HttpResponse
from rental.models import Rental


def display_table(request):
    res_set = Reservation.objects.all()
    output = ''
    prev_id = ''
    curr_ren_id = ''

    for i in range(len(res_set)):
        res = res_set[i]
        ren_id = Rental.get_id(res.rental_id)
        res_id = Reservation.get_id(res)
        if i == 0:
            curr_ren_id = ren_id
            output = output + '\n' + Reservation.get_info(res) + '|' + '-'
            prev_id = ren_id
            continue

        prev_ren_id = curr_ren_id
        curr_ren_id = ren_id
        if curr_ren_id != prev_ren_id:
            _id = '-'
            prev_id = res_id

        else:
            _id = prev_id
            prev_id = res_id

        output = output + '\n' + Reservation.get_info(res) + '|' + _id
    return HttpResponse(output)
