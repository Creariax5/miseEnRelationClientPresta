import json

from django.http import JsonResponse
from django.shortcuts import render
import requests
from .models import Trade
from .tests import give_eth, take_eth, eth_price
from .payout import payout


def pay_eth(request):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    print(f"{data['symbol']} price is {data['price']}")
    price = data['price']
    return render(request, 'pay_btc.html', context={"price": price})


def paypal(request, usd, address):
    usd = usd / 100
    print(usd)
    return render(request, 'paypal.html', context={"price": usd,
                                                   "address": address})


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

    give_eth(nb, address)

    return JsonResponse('Payment completed!', safe=False)


def eth(request, eth, address, key, email):
    current_user = request.user
    nb = eth/100
    address = address

    print("you pay ", nb)

    Trade.objects.create(
        nb=nb,
        buyer=current_user.username,
        buy_usd=True
    )

    take_eth(nb, address, key)
    value = nb * round(float(eth_price()))
    payout(email, value)

    return render(request, 'eth.html', context={"nb": nb,
                                                "usd": value})
