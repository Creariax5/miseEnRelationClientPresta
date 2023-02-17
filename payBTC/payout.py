import base64
import requests
import random


def PaypalToken(client_ID, client_Secret):
    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    data = {
        "client_id": client_ID,
        "client_secret": client_Secret,
        "grant_type": "client_credentials"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic {0}".format(
            base64.b64encode((client_ID + ":" + client_Secret).encode()).decode())
    }

    token = requests.post(url, data, headers=headers)
    return token.json()['access_token']


# DON'T FORGET TO REPLACE THE 'XXX' BELOW WITH YOUR KEYS
clientID = 'AfK20ZjlGPpSSoaMJtVV84eRIMTP1pWjxbcxFWXVPdAfGtqNnYtgLaSbKeN6WBvzLN2wRFN_LojTZNwF'
clientSecret = 'EBLiZ4DVCQOSDleTETsRJGxwg_o_k8QR6xABnTYHHyLueddW775iUqgvaaupYNZSrXiz9sWN4dfChCWM'


def create_order():
    url = 'https://api-m.sandbox.paypal.com/v2/checkout/orders'
    token = PaypalToken(clientID, clientSecret)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }
    json_data = {
        "intent": "CAPTURE",
        "application_context": {
            "notify_url": "https://pesapedia.co.ke",
            "return_url": "https://pesapedia.co.ke",  # change to your doma$
            "cancel_url": "https://pesapedia.co.ke",  # change to your domain
            "brand_name": "PESAPEDIA SANDBOX",
            "landing_page": "BILLING",
            "shipping_preference": "NO_SHIPPING",
            "user_action": "CONTINUE"
        },
        "purchase_units": [
            {
                "reference_id": "294375635",
                "description": "African Art and Collectibles",

                "custom_id": "CUST-AfricanFashion",
                "soft_descriptor": "AfricanFashions",
                "amount": {
                    "currency_code": "USD",
                    "value": "200"  # amount,
                },
            }
        ]
    }
    response = requests.post(url, headers=headers, json=json_data)
    order_id = response.json()['id']
    linkForPayment = response.json()['links'][1]['href']
    return linkForPayment


def payout(email, value):
    url = 'https://api.sandbox.paypal.com/v1/payments/payouts'
    token = PaypalToken(clientID, clientSecret)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }
    json_data = {
        "sender_batch_header": {
            "email_subject": "You have a payment",
            "sender_batch_id": "batch-" + str(random.randint(1676119897132, 9996119897132))
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": value,
                    "currency": "USD"
                },
                "receiver": email,
                "note": "Payouts sample transaction",
                "sender_item_id": "item-2-" + str(random.randint(1776119897132, 9996119897132))
            },
        ]
    }
    response = requests.post(url, headers=headers, json=json_data)
    # order_id = response.json()['id']
    # linkForPayment = response.json()['links'][1]['href']
    print(response.status_code)

    print(response.text)

    return "response"
