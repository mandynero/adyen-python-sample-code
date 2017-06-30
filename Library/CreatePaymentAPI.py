import Adyen

ady = Adyen.Adyen()

""" Create Payment through the API (Python Library)
 
	Payments can be created through our API, however this is only possible if you are PCI Compliant. Java Library payments
	are submitted using the authorise method. We will explain a simple credit card submission.
 
	Please note: using our API requires a web service user. Set up your Webservice user:
	Adyen CA >> Settings >> Users >> ws@Company. >> Generate Password >> Submit
 
	@link /2.API/Library/CreatePaymentAPI
	@author Created by Adyen - Payments Made Easy
 
"""


"""
	Client settings
         - Adyen.client
         				-username		: your web service user
                		-password		: your web service user's password
                		-platform		: the environment you are using (test/live)
                		-app_name		: your application name
"""
client = ady.client
client.username = "YourWSUser"
client.password = "YourWSPassword"
client.platform = "test"
client.app_name = "Your unique app name, to identify the app with Adyen."

"""
	A payment can be submitted to the authorise method of the library with a request,
	containing the following variables:
	
		- merchantAccount			: The merchant account for which you want to process the payment
		- amount
				- value				: The transaction amount.
				- currency			: The three character ISO currency code.
		- reference 				: Your reference for this payment.
		- ipAddress					: The shopper's IP address. (recommended)
		- shopperEmail				: The shopper's email address. (recommended)
		- shopperReference			: An ID that uniquely identifes the shopper, such as a customer id. (recommended)
		- fraudOffset				: An integer that is added to the normal fraud score. (optional)
		- card
				- number			: The card number.
				- holderName		: The card holder's name, as embossed on the card.
				- expiryMonth		: The expiration date's month written as a 2-digit string,
									padded with 0 if required (e.g. 03 or 12).
				- expiryYear		: The expiration date's year written as in full (e.g. 2016).
				- cvc 				: The card validation code, which is the CVC2 (MasterCard),
									CVV2 (Visa) or CID (American Express).
		- billingAddress (recommended)
				- street 			: The street name.
				- houseNumberOrName	: The house number (or name).
				- city				: The city.
				- postalCode		: The postal/zip code.
				- stateOrProvince 	: The state or province.
				- country 			: The country in ISO 3166-1 alpha-2 format (e.g. NL).
"""
request = {}
request['merchantAccount'] = "YourMerchantAccount"
request['amount'] = {"value":"1234","currency":"EUR"}
request['reference'] = "YourReference"
request['card'] = {
  "number":"5136333333333335",
  "expiryMonth":"08",
  "expiryYear": "2018",
  "cvc": "737",
  "holderName": "John Smith"
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
