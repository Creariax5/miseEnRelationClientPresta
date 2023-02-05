from django.shortcuts import render
import requests


def pay_btc(request):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    print(f"{data['symbol']} price is {data['price']}")
    price = data['price']
    return render(request, 'pay_btc.html', context={"price": price})
