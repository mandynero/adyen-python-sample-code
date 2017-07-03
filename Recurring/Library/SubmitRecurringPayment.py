import Adyen

ady = Adyen.Adyen()


"""Submit Recurring Payment using Python Library

You can submit a recurring payment using a specific recurringDetails record or by using the last created
recurringDetails record. The request for the recurring payment is done using a paymentRequest.
This file shows how a recurring payment can be submitted using our Python Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	Recurring/Library/SubmitRecurringPayment.py
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
A recurring payment can be submitted by sending a PaymentRequest
to the authorise action, the request should contain the following
variables:

- selectedRecurringDetailReference  : The recurringDetailReference you want to use for this payment.
                                    The value LATEST can be used to select the most recently created recurring detail.
- recurring                         : This should be the same value as recurringContract in the payment where the recurring
                                    contract was created. However if ONECLICK,RECURRING was specified initially
                                    then this field can be either ONECLICK or RECURRING.
- merchantAccount                   : The merchant account the payment was processed with.
- amount                            : The amount of the payment
    - currency                      : the currency of the payment
	- value                         : the amount of the payment
- reference                         : Your reference
- shopperEmail                      : The e-mail address of the shopper
- shopperReference                  : The shopper reference, i.e. the shopper ID
- shopperInteraction                : ContAuth for RECURRING or Ecommerce for ONECLICK
- fraudOffset                       : Numeric value that will be added to the fraud score (optional)
- shopperIP                         : The IP address of the shopper (optional)
- shopperStatement                  : Some acquirers allow you to provide a statement (optional)
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['amount'] = {"value":"1234","currency":"EUR"}
request['reference'] = "YourReference"
request["shopperEmail"] = "ref@email.com"
request["shopperReference"] = "TheShopperreference"
request["selectedRecurringDetailReference"] = "LATEST"
request["shopperInteraction"] = "ContAuth"
request['recurring'] = {}
request["recurring"]['contract'] = "RECURRING"

result = ady.payment.authorise(request)

"""        
If the payment passes validation a risk analysis will be done and, depending on the outcome, an authorisation
will be attempted. You receive a payment response with the following fields:
  - pspReference 	: Adyen's unique reference that is associated with the payment.
  - resultCode 	    : The result of the payment. Possible values: Authorised, Refused, Error or Received.
  - authCode        : The authorisation code if the payment was successful. Blank otherwise.
  - refusalReason   : Adyen's mapped refusal reason, populated if the payment was refused.
"""
print("Payment Result:")
print("- pspReference: " + result.message['pspReference'])
print("- resultCode: " + result.message['resultCode'])
print("- authCode: " + result.message['authCode'])
print("- refusalReason: " + result.message['refusalReason'])

