import json

from django.http import JsonResponse
from django.shortcuts import render
import requests
from .models import Trade
from .tests import give_btc


def pay_btc(request):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    print(f"{data['symbol']} price is {data['price']}")
    price = data['price']
    return render(request, 'pay_btc.html', context={"price": price})


def paypal(request, usd):
    usd = usd / 100
    print(usd)
    return render(request, 'paypal.html', context={"price": usd})


def compal(request):
    current_user = request.user
    body = json.loads(request.body)
    nb = body['nb']
    address = body['address']

    Trade.objects.create(
        nb=nb,
        buyer=current_user.username,
        buy_usd=False
    )

    give_btc(nb, address)

    return JsonResponse('Payment completed!', safe=False)
