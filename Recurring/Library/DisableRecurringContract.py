import Adyen

ady = Adyen.Adyen()


"""Disable recurring contract using Python Library

Disabling a recurring contract (detail) can be done by calling the disable action
on the Recurring service with a request. This file shows how you can disable
a recurring contract using Python Library.

Please note: using our API requires a web service user. Set up your Webservice
user: Adyen Test CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit

@link	Recurring/Library/DisableRecurringContract.py
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
- recurringDetailReference   : The recurringDetailReference of the details you wish to
                             disable. If you do not supply this field all details for the shopper will be disabled
                             including the contract! This means that you can not add new details anymore.
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['reference'] = "YourReference"
request["shopperEmail"] = "ref@email.com"
request["shopperReference"] = "TheShopperreference"
request['recurringDetailReference'] = "TheReferenceToTheContract"

result = ady.recurring.disable(request)

"""
The response will be a result object with a single field response. If a single detail was
disabled the value of this field will be [detail-successfully-disabled] or, if all
details are disabled, the value is [all-details-successfully-disabled].
"""

print result.message