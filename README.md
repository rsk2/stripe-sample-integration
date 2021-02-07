# stripe-sample-integration
Integration builder for stripe using HTML frontend and python backend

This repo contains the project detailed at https://stripe.com/docs/payments/integration-builder. When run it will execute a payment of $23.99 (from the calculate_order_amount() routine) and the payment will be visible on https://dashboard.stripe.com/test/payments/

**Steps to execute:**

1. Please replace the keys in main.py and client.js with your test keys present at: https://dashboard.stripe.com/account/apikeys

2. Test the integration using any of the test cards mentioned here: https://stripe.com/docs/testing#international-cards
