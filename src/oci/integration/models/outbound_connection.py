# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OutboundConnection(object):
    """
    Base representation for Outbound Connection (Reverse Connection).
    """

    #: A constant which can be used with the outbound_connection_type property of a OutboundConnection.
    #: This constant has a value of "PRIVATE_ENDPOINT"
    OUTBOUND_CONNECTION_TYPE_PRIVATE_ENDPOINT = "PRIVATE_ENDPOINT"

    #: A constant which can be used with the outbound_connection_type property of a OutboundConnection.
    #: This constant has a value of "NONE"
    OUTBOUND_CONNECTION_TYPE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new OutboundConnection object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.integration.models.PrivateEndpointOutboundConnection`
        * :class:`~oci.integration.models.NoneOutboundConnection`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param outbound_connection_type:
            The value to assign to the outbound_connection_type property of this OutboundConnection.
            Allowed values for this property are: "PRIVATE_ENDPOINT", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type outbound_connection_type: str

        """
        self.swagger_types = {
            'outbound_connection_type': 'str'
        }

        self.attribute_map = {
            'outbound_connection_type': 'outboundConnectionType'
        }

        self._outbound_connection_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['outboundConnectionType']

        if type == 'PRIVATE_ENDPOINT':
            return 'PrivateEndpointOutboundConnection'

        if type == 'NONE':
            return 'NoneOutboundConnection'
        else:
            return 'OutboundConnection'

    @property
    def outbound_connection_type(self):
        """
        **[Required]** Gets the outbound_connection_type of this OutboundConnection.
        The type of Outbound Connection.

        Allowed values for this property are: "PRIVATE_ENDPOINT", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The outbound_connection_type of this OutboundConnection.
        :rtype: str
        """
        return self._outbound_connection_type

    @outbound_connection_type.setter
    def outbound_connection_type(self, outbound_connection_type):
        """
        Sets the outbound_connection_type of this OutboundConnection.
        The type of Outbound Connection.


        :param outbound_connection_type: The outbound_connection_type of this OutboundConnection.
        :type: str
        """
        allowed_values = ["PRIVATE_ENDPOINT", "NONE"]
        if not value_allowed_none_or_none_sentinel(outbound_connection_type, allowed_values):
            outbound_connection_type = 'UNKNOWN_ENUM_VALUE'
        self._outbound_connection_type = outbound_connection_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other