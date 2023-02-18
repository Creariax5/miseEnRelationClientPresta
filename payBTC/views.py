import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
    eth = round(float(eth_price()), 2)
    my_eth = round(float(usd) / float(eth), 6)
    return render(request, 'paypal.html', context={"price": usd,
                                                   "eth": eth,
                                                   "my_eth": my_eth,
                                                   "address": address})


def paypal_success(request):
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
    value = round(nb / float(eth_price()), 6)
    url = '/pay_btc/complete_buy/' + str(nb) + "/" + str(value) + "/"

    return JsonResponse({"url": url})


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

    return redirect('/pay_btc/complete_sell/' + str(nb) + "/" + str(value) + "/")


def complete_buy(request, nb, value):
    ph = "Congrats ! " + str(nb) + " USD was converted in " + str(value) + " ETH and sent to your ETH address !"
    return render(request, 'eth.html', context={"phrase": ph})


def complete_sell(request, nb, value):
    ph = "Congrats ! " + str(nb) + " ETH was converted in " + str(value) + " dollars and added to your paypal account !"
    return render(request, 'eth.html', context={"phrase": ph})


def react(request):

    return render(request, 'react_app/build/index.html', context={"qui": "django"})


def is_authenticated(request):
    authenticated = False
    if request.user.is_authenticated:
        authenticated = True
    data = {
        'authenticated': authenticated
    }
    return JsonResponse(data)
