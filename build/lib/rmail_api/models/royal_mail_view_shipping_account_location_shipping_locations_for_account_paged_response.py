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

class RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse(object):
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
        'shipping_locations': 'list[RoyalMailViewShippingAccountLocationShippingLocationForAccount]',
        'total_count': 'int'
    }

    attribute_map = {
        'shipping_locations': 'ShippingLocations',
        'total_count': 'TotalCount'
    }

    def __init__(self, shipping_locations=None, total_count=None):  # noqa: E501
        """RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse - a model defined in Swagger"""  # noqa: E501
        self._shipping_locations = None
        self._total_count = None
        self.discriminator = None
        self.shipping_locations = shipping_locations
        self.total_count = total_count

    @property
    def shipping_locations(self):
        """Gets the shipping_locations of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.  # noqa: E501

        Shipping Locations <br />The shipping locations for the requested page only.  # noqa: E501

        :return: The shipping_locations of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.  # noqa: E501
        :rtype: list[RoyalMailViewShippingAccountLocationShippingLocationForAccount]
        """
        return self._shipping_locations

    @shipping_locations.setter
    def shipping_locations(self, shipping_locations):
        """Sets the shipping_locations of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.

        Shipping Locations <br />The shipping locations for the requested page only.  # noqa: E501

        :param shipping_locations: The shipping_locations of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.  # noqa: E501
        :type: list[RoyalMailViewShippingAccountLocationShippingLocationForAccount]
        """
        if shipping_locations is None:
            raise ValueError("Invalid value for `shipping_locations`, must not be `None`")  # noqa: E501

        self._shipping_locations = shipping_locations

    @property
    def total_count(self):
        """Gets the total_count of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.  # noqa: E501

        Total Count <br />The total number of locations available  # noqa: E501

        :return: The total_count of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.

        Total Count <br />The total number of locations available  # noqa: E501

        :param total_count: The total_count of this RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if issubclass(RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse, dict):
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
        if not isinstance(other, RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
