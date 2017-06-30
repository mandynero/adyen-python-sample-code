import Adyen

ady = Adyen.Adyen()

""" Create Client-Side Encryption Payment (Python Library)
    
Merchants that require more stringent security protocols or do not want the additional overhead
of managing their PCI compliance, may decide to implement Client-Side Encryption (CSE).
This is particularly useful for Mobile payment flows where only cards are being offered, as
it may result in faster load times and an overall improvement to the shopper flow.
The Adyen Hosted Payment Page (HPP) provides the most comprehensive level of PCI compliancy
and you do not have any PCI obligations. Using CSE reduces your PCI scope when compared to
implementing the API without encryption.

If you would like to implement CSE, please provide the completed PCI Self Assessment Questionnaire (SAQ)
A to the Adyen Support Team (support@adyen.com). The form can be found here:
https://www.pcisecuritystandards.org/security_standards/documents.php?category=saqs

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	API/Library/CreatePaymentCSE.py
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
The payment can be submitted by sending a PaymentRequest
to the authorise action of the web service, the request should
contain the following variables:
- merchantAccount           : The merchant account the payment was processed with.
- amount
    - currency              : the currency of the payment
    - value                 : the amount of the payment
- reference                 : Your reference
- shopperIP                 : The IP address of the shopper (optional/recommended)
- shopperEmail              : The e-mail address of the shopper
- shopperReference          : The shopper reference, i.e. the shopper ID
- fraudOffset               : Numeric value that will be added to the fraud score (optional)
- additionalData
  - card.encrypted.json     : The encrypted card catched by the POST variables.
"""

request = {}
request['amount'] = {"value": "1234", "currency": "EUR"}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request['additionalData'] = {
    "card.encrypted.json" : "YourCSEToken"
    }

result = ady.payment.authorise(request)

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