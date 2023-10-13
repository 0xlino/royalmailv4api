# coding: utf-8

"""
    PRO SHIPPING API

    # Introduction Here you will find requirements for integrating with PRO SHIPPING API.  The documentation specifically covers how the API can be used by business customers to conduct shipping activity with available carriers and provides the technical information to build this integration. The API allows customers to create and manage shipments, produce labels, customs documentation, and collection manifests, retrieve reference data such as carriers and countries, and maintain their own data such as shipping account details.  Pro Shipping API is a fully RESTful service implemented using JSON messaging. You, as the customer are responsible for sending JSON messages and for maintaining the capability of receiving JSON messages in the format described in this specification. Request and response examples for each API service are included in this specification.  # Authentication  The PRO SHIPPING API uses OAuth2 authentication.  To request the authorization token you need to create API credentials (Client ID and Secret) on the system first. If you have not done it already, log into your account and go to API Credentials or follow the link [add a link here with the path to the API Credentials menu]. Use the credentials to retrieve the authorization token.  Note: Make sure you copy the Secret and keep it secure as you won't be able to view it again on the system.  <!-- ReDoc-Inject: <SecurityDefinitions /> -->   # noqa: E501

    OpenAPI spec version: v4.0-RM
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RoyalMailShippingAccount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'shipping_account_id': 'str',
        'carrier_code': 'str',
        'account_number': 'str',
        'account_type': 'AccountType',
        'account_name': 'str',
        'account_registered_email': 'str',
        'account_alias': 'str',
        'account_status': 'str',
        'contact_name': 'str',
        'contact_number': 'str',
        'last_updated_by': 'str',
        'last_updated_date_utc': 'datetime'
    }

    attribute_map = {
        'shipping_account_id': 'ShippingAccountId',
        'carrier_code': 'CarrierCode',
        'account_number': 'AccountNumber',
        'account_type': 'AccountType',
        'account_name': 'AccountName',
        'account_registered_email': 'AccountRegisteredEmail',
        'account_alias': 'AccountAlias',
        'account_status': 'AccountStatus',
        'contact_name': 'ContactName',
        'contact_number': 'ContactNumber',
        'last_updated_by': 'LastUpdatedBy',
        'last_updated_date_utc': 'LastUpdatedDateUtc'
    }

    def __init__(self, shipping_account_id=None, carrier_code=None, account_number=None, account_type=None, account_name=None, account_registered_email=None, account_alias=None, account_status=None, contact_name=None, contact_number=None, last_updated_by=None, last_updated_date_utc=None):  # noqa: E501
        """RoyalMailShippingAccount - a model defined in Swagger"""  # noqa: E501
        self._shipping_account_id = None
        self._carrier_code = None
        self._account_number = None
        self._account_type = None
        self._account_name = None
        self._account_registered_email = None
        self._account_alias = None
        self._account_status = None
        self._contact_name = None
        self._contact_number = None
        self._last_updated_by = None
        self._last_updated_date_utc = None
        self.discriminator = None
        self.shipping_account_id = shipping_account_id
        self.carrier_code = carrier_code
        if account_number is not None:
            self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.account_registered_email = account_registered_email
        self.account_alias = account_alias
        self.account_status = account_status
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.last_updated_by = last_updated_by
        self.last_updated_date_utc = last_updated_date_utc

    @property
    def shipping_account_id(self):
        """Gets the shipping_account_id of this RoyalMailShippingAccount.  # noqa: E501

        Shipping Account Id <br />The system identifier for this account. <br />Use one of the Id or Alias in the Create Shipment Request to identify the account to use.  # noqa: E501

        :return: The shipping_account_id of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._shipping_account_id

    @shipping_account_id.setter
    def shipping_account_id(self, shipping_account_id):
        """Sets the shipping_account_id of this RoyalMailShippingAccount.

        Shipping Account Id <br />The system identifier for this account. <br />Use one of the Id or Alias in the Create Shipment Request to identify the account to use.  # noqa: E501

        :param shipping_account_id: The shipping_account_id of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if shipping_account_id is None:
            raise ValueError("Invalid value for `shipping_account_id`, must not be `None`")  # noqa: E501

        self._shipping_account_id = shipping_account_id

    @property
    def carrier_code(self):
        """Gets the carrier_code of this RoyalMailShippingAccount.  # noqa: E501

        Carrier Code <br />The carrier that this shipping account is for.  # noqa: E501

        :return: The carrier_code of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this RoyalMailShippingAccount.

        Carrier Code <br />The carrier that this shipping account is for.  # noqa: E501

        :param carrier_code: The carrier_code of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if carrier_code is None:
            raise ValueError("Invalid value for `carrier_code`, must not be `None`")  # noqa: E501

        self._carrier_code = carrier_code

    @property
    def account_number(self):
        """Gets the account_number of this RoyalMailShippingAccount.  # noqa: E501

        Carrier Account Number <br />The account number given by the carrier.  # noqa: E501

        :return: The account_number of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this RoyalMailShippingAccount.

        Carrier Account Number <br />The account number given by the carrier.  # noqa: E501

        :param account_number: The account_number of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def account_type(self):
        """Gets the account_type of this RoyalMailShippingAccount.  # noqa: E501


        :return: The account_type of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: AccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this RoyalMailShippingAccount.


        :param account_type: The account_type of this RoyalMailShippingAccount.  # noqa: E501
        :type: AccountType
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def account_name(self):
        """Gets the account_name of this RoyalMailShippingAccount.  # noqa: E501

        Shipping Account Name <br />The name of the Shipping Account.  # noqa: E501

        :return: The account_name of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this RoyalMailShippingAccount.

        Shipping Account Name <br />The name of the Shipping Account.  # noqa: E501

        :param account_name: The account_name of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_registered_email(self):
        """Gets the account_registered_email of this RoyalMailShippingAccount.  # noqa: E501

        Account Registered Email <br />This is the email that was used to register your Shipping Account with the carrier when the Shipping Account was created.  # noqa: E501

        :return: The account_registered_email of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_registered_email

    @account_registered_email.setter
    def account_registered_email(self, account_registered_email):
        """Sets the account_registered_email of this RoyalMailShippingAccount.

        Account Registered Email <br />This is the email that was used to register your Shipping Account with the carrier when the Shipping Account was created.  # noqa: E501

        :param account_registered_email: The account_registered_email of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if account_registered_email is None:
            raise ValueError("Invalid value for `account_registered_email`, must not be `None`")  # noqa: E501

        self._account_registered_email = account_registered_email

    @property
    def account_alias(self):
        """Gets the account_alias of this RoyalMailShippingAccount.  # noqa: E501

        Shipping Account Alias <br />Your identifier for this account. Must be unique.  # noqa: E501

        :return: The account_alias of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_alias

    @account_alias.setter
    def account_alias(self, account_alias):
        """Sets the account_alias of this RoyalMailShippingAccount.

        Shipping Account Alias <br />Your identifier for this account. Must be unique.  # noqa: E501

        :param account_alias: The account_alias of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if account_alias is None:
            raise ValueError("Invalid value for `account_alias`, must not be `None`")  # noqa: E501

        self._account_alias = account_alias

    @property
    def account_status(self):
        """Gets the account_status of this RoyalMailShippingAccount.  # noqa: E501

        Account Status <br />The status of the shipping account.  # noqa: E501

        :return: The account_status of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """Sets the account_status of this RoyalMailShippingAccount.

        Account Status <br />The status of the shipping account.  # noqa: E501

        :param account_status: The account_status of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if account_status is None:
            raise ValueError("Invalid value for `account_status`, must not be `None`")  # noqa: E501

        self._account_status = account_status

    @property
    def contact_name(self):
        """Gets the contact_name of this RoyalMailShippingAccount.  # noqa: E501

        Contact Name <br />Used in a create shipment request as the shipper's contact name if the shipper address is not provided.  # noqa: E501

        :return: The contact_name of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this RoyalMailShippingAccount.

        Contact Name <br />Used in a create shipment request as the shipper's contact name if the shipper address is not provided.  # noqa: E501

        :param contact_name: The contact_name of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if contact_name is None:
            raise ValueError("Invalid value for `contact_name`, must not be `None`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def contact_number(self):
        """Gets the contact_number of this RoyalMailShippingAccount.  # noqa: E501

        Contact Number <br />Used in a create shipment request as the shipper's contact number if the shipper address is not provided, and the contact number is not set on the associated shipping location.  # noqa: E501

        :return: The contact_number of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """Sets the contact_number of this RoyalMailShippingAccount.

        Contact Number <br />Used in a create shipment request as the shipper's contact number if the shipper address is not provided, and the contact number is not set on the associated shipping location.  # noqa: E501

        :param contact_number: The contact_number of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if contact_number is None:
            raise ValueError("Invalid value for `contact_number`, must not be `None`")  # noqa: E501

        self._contact_number = contact_number

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this RoyalMailShippingAccount.  # noqa: E501

        Last Updated By <br />The user that last updated the shipping account.  # noqa: E501

        :return: The last_updated_by of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this RoyalMailShippingAccount.

        Last Updated By <br />The user that last updated the shipping account.  # noqa: E501

        :param last_updated_by: The last_updated_by of this RoyalMailShippingAccount.  # noqa: E501
        :type: str
        """
        if last_updated_by is None:
            raise ValueError("Invalid value for `last_updated_by`, must not be `None`")  # noqa: E501

        self._last_updated_by = last_updated_by

    @property
    def last_updated_date_utc(self):
        """Gets the last_updated_date_utc of this RoyalMailShippingAccount.  # noqa: E501

        Last Updated Date UTC <br />The system date and time when the shipping account was last updated.  # noqa: E501

        :return: The last_updated_date_utc of this RoyalMailShippingAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date_utc

    @last_updated_date_utc.setter
    def last_updated_date_utc(self, last_updated_date_utc):
        """Sets the last_updated_date_utc of this RoyalMailShippingAccount.

        Last Updated Date UTC <br />The system date and time when the shipping account was last updated.  # noqa: E501

        :param last_updated_date_utc: The last_updated_date_utc of this RoyalMailShippingAccount.  # noqa: E501
        :type: datetime
        """
        if last_updated_date_utc is None:
            raise ValueError("Invalid value for `last_updated_date_utc`, must not be `None`")  # noqa: E501

        self._last_updated_date_utc = last_updated_date_utc

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RoyalMailShippingAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RoyalMailShippingAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
