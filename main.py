#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe
# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'ENTERYOURKEY'

from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_url_path="")

def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 2399

@app.route('/')
def home():
    return render_template("checkout.html")

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        #print("inside create_payment")
        data = json.loads(request.data)    
        print(data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )
        print(intent['client_secret'])
        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(debug=True)

