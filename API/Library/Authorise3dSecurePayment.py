import Adyen

ady = Adyen.Adyen()

"""Authorise 3D Secure payment (Python Library)

3D Secure (Verifed by VISA / MasterCard SecureCode™) is an additional authentication
protocol that involves the shopper being redirected to their card issuer where their
identity is authenticated prior to the payment proceeding to an authorisation request.

In order to start processing 3D Secure transactions, the following changes are required:
1. Your Merchant Account needs to be confgured by Adyen to support 3D Secure. If you would
   like to have 3D Secure enabled, please submit a request to the Adyen Support Team (support@adyen.com).
2. Your integration should support redirecting the shopper to the card issuer and submitting
   a second API call to complete the payment.

This example demonstrates the second API call to complete the payment using Python Library.
See the API Manual for a full explanation of the steps required to process 3D Secure payments.

Please note: using our API requires a web service user. Set up your Webservice user:
Adyen CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	API/Library/Authorise3dSecurePayment.py
@author	Created by Adyen
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
After the shopper's identity is authenticated by the issuer, they will be returned to your
site by sending an HTTP POST request to the TermUrl containing the MD parameter and a new
parameter called PaRes (see API manual). These will be needed to complete the payment.

To complete the payment, a PaymentRequest3d should be submitted to the authorise3d action
of the web service. The request should contain the following variables:

- merchantAccount             : This should be the same as the Merchant Account used in the original authorise request.
- browserInfo                 : It is safe to use the values from the original authorise request, as they
                                are unlikely to change during the course of a payment.
- md                          : The value of the MD parameter received from the issuer.
- paResponse                  : The value of the PaRes parameter received from the issuer.
- shopperIP                   : The IP address of the shopper. We recommend that you provide this data, as
                                it is used in a number of risk checks, for example, the number of payment
                                attempts and location based checks.

"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request['browserInfo'] = {
    "userAgent" : "YourUserAgent",
    "acceptHeader" : "YourAcceptHeader"
  }
request['md'] = "YourMd"
request['paResponse'] = "YourPaResponse"

result = ady.payment.authorise3d(request)

"""        
If the payment passes validation a risk analysis will be done and, depending on the outcome, an authorisation
will be attempted. You receive a payment response with the following fields:
  - pspReference 	: Adyen's unique reference that is associated with the payment.
  - resultCode 	: The result of the payment. Possible values: Authorised, Refused, Error or Received.
  - authCode      : The authorisation code if the payment was successful. Blank otherwise.
  - refusalReason: Adyen's mapped refusal reason, populated if the payment was refused.
"""

print("Payment Result:")
print("- pspReference: " + result.message['pspReference'])
print("- resultCode: " + result.message['resultCode'])
print("- authCode: " + result.message['authCode'])
print("- refusalReason: " + result.message['refusalReason'])