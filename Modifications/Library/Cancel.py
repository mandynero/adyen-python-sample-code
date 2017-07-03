import Adyen

ady = Adyen.Adyen()

"""Cancel a Payment using Python Library

In order to cancel an authorised (card) payment you send a modification
request to the cancel action. This file shows how an authorised payment
should be canceled by sending a modification request using Python Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	Modifications/Library/Cancel.py
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
Perform cancel request by sending in a
modificationRequest. The following parameters are used:
- merchantAccount            : The merchant account the payment was processed with.
- originalReference          : This is the pspReference that was assigned to the authorisation
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request['originalReference'] = "YourOriginalReference"
result = ady.payment.cancel(request)

"""
If the message was syntactically valid and merchantAccount is correct you will
receive a cancelReceived response with the following fields:
- pspReference               : A new reference to uniquely identify this modification request.
- response                   : A confirmation indicating we received the request: [cancel-received].

Please note: The result of the cancellation is sent via a notification with eventCode CANCELLATION.
"""
print("Modification Result:")
print("- pspReference: " + result.message['pspReference'])
print("- response: " + result.message['response'])