import Adyen

ady = Adyen.Adyen()


"""Request recurring contract details using Python Library

Once a shopper has stored RECURRING details with Adyen you are able to process
a RECURRING payment. This file shows you how to retrieve the RECURRING contract(s)
for a shopper using Python Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	Recurring/Library/RequestRecurringContract.py
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
The request should contain the following variables:
- merchantAccount            : The merchant account the payment was processed with.
- shopperReference           : The reference to the shopper. This shopperReference must be the same as the
                             shopperReference used in the initial payment.
- recurring['contract']      : This should be the same value as recurringContract in the payment where the recurring
                             contract was created. However if ONECLICK,RECURRING was specified initially
                             then this field can be either ONECLICK or RECURRING.
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request["shopperEmail"] = "ref@email.com"
request["shopperReference"] = "TheShopperreference"
request['recurring'] = {}
request["recurring"]['contract'] = "RECURRING"

result = ady.recurring.list_recurring_details(request)

"""
The response will be a result with a list of zero or more details containing at least the following:
- recurringDetailReference   : The reference the details are stored under.
- variant                    : The payment method (e.g. mc, visa, elv, ideal, paypal)
- creationDate               : The date when the recurring details were created.

The recurring contracts are stored in the same object types as you would have
submitted in the initial payment.
"""

print result.message