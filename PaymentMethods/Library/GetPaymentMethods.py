import Adyen
import pprint
import time

ady = Adyen.Adyen()

"""Get Payment Methods

Optionally the payment method selection page can be skipped, so the shopper
starts directly on the payment details entry page. This is done by calling
details.shtml instead of select.shtml. A further parameter, brandCode,
should be supplied with the payment method chosen (see Payment Methods section
for more details, but note that the group values are not valid).

The directory service can also be used to request which payment methods
are available for the shopper on your specific merchant account.
This is done by calling directory.shtml with a normal payment request.
This file provides a code example showing how to retreive the
payment methods enabled for the specified merchant account.

Please note that the countryCode field is mandatory to receive
back the correct payment methods.

@link	PaymentMethods/Library/GetPaymentMethods.py
@author	Created by Adyen - Payments Made Easy
"""

"""
Client settings
 - Adyen.client
  - platform	: the environment you are using (test/live)
  - app_name	: your application name
  - hmac        : your hmac key
"""
client = ady.client
client.platform = "test"
client.app_name = "Your unique app name, to identify the app with Adyen."
client.hmac = "YourHmacKey"

"""
Payment Request
The following fields are required for the directory
service.
"""

request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['paymentAmount'] = "1000"
request['currencyCode'] = "EUR"
request['merchantReference'] = "Get Payment methods"
request['skinCode'] = "YourSkinCode"
request['countryCode'] = "NL"
request['shopperLocale'] = "nl_NL"
request['sessionValidity'] = time.strftime('%Y-%m-%dT%H:%M:%SZ')

result = self.ady.hpp.directory_lookup(self.request)

"""
The $result contains a JSON array containing
the available payment methods for the merchant account.
"""
pp = pprint.PrettyPrinter()
pp.pprint (result.message)