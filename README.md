Adyen Python Integration
==============
The code examples in this repository help you integrate with the [Adyen platform](https://www.adyen.com) using Python. Please go through these code examples and read the documentation in the files itself.

Each code example requires you to change some parameters to connect to your Adyen account (such as a merchant account and skin code).


## Python API Library
We have made a library available that contains all of these APIs to make the integration easier. The Library is open-source and available [here](https://github.com/Adyen/adyen-python-api-library).

## Code structure
```
API
  - Library
    - Authorise3dSecurePayment.py    : Authorise a 3D Secure payment using Python Library
    - Create3dSecurePayment.py       : Create a 3D Secure payment using Python Library
    - CreatePaymentAPI.py            : Create a payment via our API using Python Library
    - CreatePaymentCSE.py            : Create a Client-Side Encrypted payment using Python Library
Modifications
  - Library
    - CancelOrRefund.py              : Cancel or refund a payment using Python Library
    - Cancel.py                      : Cancel a payment using Python Library
    - Capture.py                     : Capture a payment using Python Library
    - Refund.py                      : Request a refund using Python Library
Recurring
  - Library
    - SubmitRecurringPayment.py      : Create a recurring payment using Python Library
    - DisableRecurringContract.py    : Disable a recurring contract for a shopper using Python Library
    - RequestRecurringContract.py    : Request a recurring contact for a shopper using Python Library
PaymentMethods
  -Library
    - GetPaymentMethods.py           : Get payment methods available for merchant account using Python Library
```
## Documentation
The code examples are based on our developer documentation, which provides comprehensive information on how the Adyen platform works. For more information, refer to the [Adyen Documentation](https://docs.adyen.com/).

## Questions?
If you have any questions or suggestions regarding this repository, please contact us at support@adyen.com.
