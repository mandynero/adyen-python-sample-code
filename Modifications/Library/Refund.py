import Adyen

ady = Adyen.Adyen()

"""Refund a Payment using Python Library

Settled payments can be refunded by sending a modifiction request
to the refund action. This file shows how a settled payment
can be refunded by sending a modification request using Python Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	Modifications/Library/Refund.py
@author	Created by Adyen - Payments Made Easy
"""

"""
Client settings
 - Adyen.client
  - username    : your web service user
  - password	: your web service user's password
  - platform	: the environment you are using (test/live)
  - app_name	: your application name
"""
client = ady.client
client.username = "YourWSUser"
client.password = "YourWSPassword"
client.platform = "test"
client.app_name = "Your unique app name, to identify the app with Adyen."

"""
Perform refund request by sending in a
modificationRequest. The following parameters are used:
- merchantAccount           : The merchant account the payment was processed with.
- modificationAmount        : The amount to refund
    - currency              : the currency must match the original payment
    - value                 : the value must be the same or less than the original amount
- originalReference         : This is the pspReference that was assigned to the authorisation
- reference                 : If you wish, you can to assign your own reference or description to the modification.
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request['modificationAmount'] = {"value": "1234", "currency": "EUR"}
request['originalReference'] = "YourOriginalReference"
result = ady.payment.refund(request)

"""
If the message was syntactically valid and merchantAccount is correct you will
receive a refundReceived response with the following fields:
- pspReference              : A new reference to uniquely identify this modification request.
- response                  : A confirmation indicating we received the request: [refund-received].

Please note: The result of the refund is sent via a notification with eventCode REFUND.
"""

print("Modification Result:")
print("- pspReference: " + result.message['pspReference'])
print("- response: " + result.message['response'])