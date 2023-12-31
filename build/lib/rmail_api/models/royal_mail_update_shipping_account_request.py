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

class RoyalMailUpdateShippingAccountRequest(object):
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
        'account_registered_email': 'str',
        'account_number': 'str',
        'account_type': 'AccountType',
        'account_name': 'str',
        'account_alias': 'str',
        'contact_name': 'str',
        'contact_number': 'str'
    }

    attribute_map = {
        'account_registered_email': 'AccountRegisteredEmail',
        'account_number': 'AccountNumber',
        'account_type': 'AccountType',
        'account_name': 'AccountName',
        'account_alias': 'AccountAlias',
        'contact_name': 'ContactName',
        'contact_number': 'ContactNumber'
    }

    def __init__(self, account_registered_email=None, account_number=None, account_type=None, account_name=None, account_alias=None, contact_name=None, contact_number=None):  # noqa: E501
        """RoyalMailUpdateShippingAccountRequest - a model defined in Swagger"""  # noqa: E501
        self._account_registered_email = None
        self._account_number = None
        self._account_type = None
        self._account_name = None
        self._account_alias = None
        self._contact_name = None
        self._contact_number = None
        self.discriminator = None
        self.account_registered_email = account_registered_email
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.account_alias = account_alias
        self.contact_name = contact_name
        self.contact_number = contact_number

    @property
    def account_registered_email(self):
        """Gets the account_registered_email of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501

        Account Registered Email <br />This is the email that was used to register your Shipping Account with the carrier when the Shipping Account was created.  # noqa: E501

        :return: The account_registered_email of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_registered_email

    @account_registered_email.setter
    def account_registered_email(self, account_registered_email):
        """Sets the account_registered_email of this RoyalMailUpdateShippingAccountRequest.

        Account Registered Email <br />This is the email that was used to register your Shipping Account with the carrier when the Shipping Account was created.  # noqa: E501

        :param account_registered_email: The account_registered_email of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: str
        """
        if account_registered_email is None:
            raise ValueError("Invalid value for `account_registered_email`, must not be `None`")  # noqa: E501

        self._account_registered_email = account_registered_email

    @property
    def account_number(self):
        """Gets the account_number of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501

        Carrier Account Number  # noqa: E501

        :return: The account_number of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this RoyalMailUpdateShippingAccountRequest.

        Carrier Account Number  # noqa: E501

        :param account_number: The account_number of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def account_type(self):
        """Gets the account_type of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501


        :return: The account_type of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: AccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this RoyalMailUpdateShippingAccountRequest.


        :param account_type: The account_type of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: AccountType
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def account_name(self):
        """Gets the account_name of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501

        Account Name <br />The name on this Account.  # noqa: E501

        :return: The account_name of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this RoyalMailUpdateShippingAccountRequest.

        Account Name <br />The name on this Account.  # noqa: E501

        :param account_name: The account_name of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_alias(self):
        """Gets the account_alias of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501

        Account Alias <br />Your identifier for this account. Must be unique.  # noqa: E501

        :return: The account_alias of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_alias

    @account_alias.setter
    def account_alias(self, account_alias):
        """Sets the account_alias of this RoyalMailUpdateShippingAccountRequest.

        Account Alias <br />Your identifier for this account. Must be unique.  # noqa: E501

        :param account_alias: The account_alias of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: str
        """
        if account_alias is None:
            raise ValueError("Invalid value for `account_alias`, must not be `None`")  # noqa: E501

        self._account_alias = account_alias

    @property
    def contact_name(self):
        """Gets the contact_name of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501

        Contact Name <br />Used in a create shipment request as the shipper's contact name if the shipper address is not provided.  # noqa: E501

        :return: The contact_name of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this RoyalMailUpdateShippingAccountRequest.

        Contact Name <br />Used in a create shipment request as the shipper's contact name if the shipper address is not provided.  # noqa: E501

        :param contact_name: The contact_name of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: str
        """
        if contact_name is None:
            raise ValueError("Invalid value for `contact_name`, must not be `None`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def contact_number(self):
        """Gets the contact_number of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501

        Contact Number <br />Used in a create shipment request as the shipper's contact number if the shipper address is not provided, and the contact number is not set on the associated shipping location.  # noqa: E501

        :return: The contact_number of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """Sets the contact_number of this RoyalMailUpdateShippingAccountRequest.

        Contact Number <br />Used in a create shipment request as the shipper's contact number if the shipper address is not provided, and the contact number is not set on the associated shipping location.  # noqa: E501

        :param contact_number: The contact_number of this RoyalMailUpdateShippingAccountRequest.  # noqa: E501
        :type: str
        """
        if contact_number is None:
            raise ValueError("Invalid value for `contact_number`, must not be `None`")  # noqa: E501

        self._contact_number = contact_number

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
        if issubclass(RoyalMailUpdateShippingAccountRequest, dict):
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
        if not isinstance(other, RoyalMailUpdateShippingAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
