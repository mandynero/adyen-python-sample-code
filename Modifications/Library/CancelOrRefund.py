import Adyen

ady = Adyen.Adyen()


"""Cancel or Refund a Payment using PHP Library

If you do not know if the payment is captured but you want to reverse
the authorisation you can send a modification request to the cancelOrRefund action
This file shows how a payment can be cancelled or refunded by a
modification request using PHP Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	4.Modifications/Library/cancel-or-refund.php
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
Perform cancel or refund request by sending in a
modificationRequest. The following parameters are used:
- merchantAccount            : The merchant account the payment was processed with.
- originalReference          : This is the pspReference that was assigned to the authorisation
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request['originalReference'] = "YourOriginalReference"
result = ady.payment.cancel_or_refund(request)

"""
If the message was syntactically valid and merchantAccount is correct you will receive a
cancelOrRefundReceived response with the following fields:
- pspReference               : A new reference to uniquely identify this modification request.
- response                   : A confirmation indicating we received the request: [cancelOrRefund-received].

If the payment is authorised, but not yet captured, it will be cancelled.
In other cases the payment will be fully refunded (if possible).

Please note: The actual result of the cancel or refund is sent via a notification with eventCode CANCEL_OR_REFUND.
"""

print("Modification Result:")
print("- pspReference: " + result.message['pspReference'])
print("- response: " + result.message['response'])