import json

from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from django.conf import settings
from django.http import HttpResponse

from orders.models import Order


def payment_process(request):
    # Get order id from session :
    order_id = request.session.get('order_id')
    # Get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = order.get_total_price() * 10

    zarinpal_request_url = "https://api.zarinpal.com/pg/v4/payment/request.json"

    request_header = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f'#{order.id} : {order.user.first_name} {order.user.last_name}',
        'callback_url': request.build_absolute_uri(reverse("payment:payment_callback")),
    }

    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
    print(res.json())
    data = res.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse('ERROR FROM ZARINPAL')


def payment_callback(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('Status')

    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = order.get_total_price() * 10

    if payment_status == 'OK':

        request_header = {
            "accept": "application/json",
            "content-type": "application/json",
        }

        request_data = {
            'merchant_id': settings.ZARINPAL_MERCHANT_ID,
            'amount': rial_total_price,
            'authority' : payment_authority,
        }

        res = requests.post(
            url='https://api.zarinpal.com/pg/v4/payment/verify.json',
            data=json.dumps(request_data),
            headers= request_header,
        )

        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['data']['errors'])):
            data = res.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()

                return HttpResponse("تراکنش با موفقیت انجام شد")

            elif payment_code == 101:
                return HttpResponse("تراکنش تکراری")

            else:
                error_code = res.json()['errors']['code']
                error_message = res.json()['error']['message']
                return HttpResponse(f"تراکنش ناموفق {error_message}{error_code}")

    else:
        return HttpResponse('پرداخت ناموفق')