import Adyen

ady = Adyen.Adyen()

""" Capture a Payment using Python Library

Authorised (card) payments can be captured to get the money from the shopper.
Payments can be automatically captured by our platform. A payment can
also be captured by performing an API call. In order to capture an authorised
(card) payment you have to send a modification request. This file
shows how an authorised payment should be captured by sending
a modification request using Python Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	Modifications/Library/Capture.py
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
Perform capture request by sending in a
modificationRequest. The following parameters are used:
- merchantAccount           : The merchant account the payment was processed with.
- modificationAmount        : The amount to capture
    - currency              : the currency must match the original payment
    - value                 : the value must be the same or less than the original amount
- originalReference         : This is the pspReference that was assigned to the authorisation
- reference                 : If you wish, you can assign your own reference or description to the modification.
"""
request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request['modificationAmount'] = {"value": "1234", "currency": "EUR"}
request['originalReference'] = "YourOriginalReference"
result = ady.payment.capture(request)

"""
If the message was syntactically valid and merchantAccount is correct you will
receive a captureResult response with the following fields:
- pspReference               : A new reference to uniquely identify this modification request.
- response                   : A confirmation indicating we received the request: [capture-received].

Please note: The result of the capture is sent via a notification with eventCode CAPTURE.
"""
print("Modification Result:")
print("- pspReference: " + result.message['pspReference'])
print("- response: " + result.message['response'])

