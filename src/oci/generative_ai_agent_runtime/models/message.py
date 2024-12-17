# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Message(object):
    """
    The Message resource generated by the agent.
    """

    #: A constant which can be used with the role property of a Message.
    #: This constant has a value of "USER"
    ROLE_USER = "USER"

    #: A constant which can be used with the role property of a Message.
    #: This constant has a value of "AGENT"
    ROLE_AGENT = "AGENT"

    def __init__(self, **kwargs):
        """
        Initializes a new Message object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this Message.
            Allowed values for this property are: "USER", "AGENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param content:
            The value to assign to the content property of this Message.
        :type content: oci.generative_ai_agent_runtime.models.MessageContent

        :param time_created:
            The value to assign to the time_created property of this Message.
        :type time_created: datetime

        """
        self.swagger_types = {
            'role': 'str',
            'content': 'MessageContent',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'role': 'role',
            'content': 'content',
            'time_created': 'timeCreated'
        }

        self._role = None
        self._content = None
        self._time_created = None

    @property
    def role(self):
        """
        **[Required]** Gets the role of this Message.
        The role of the sender of this message.

        Allowed values for this property are: "USER", "AGENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this Message.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Message.
        The role of the sender of this message.


        :param role: The role of this Message.
        :type: str
        """
        allowed_values = ["USER", "AGENT"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def content(self):
        """
        **[Required]** Gets the content of this Message.

        :return: The content of this Message.
        :rtype: oci.generative_ai_agent_runtime.models.MessageContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Message.

        :param content: The content of this Message.
        :type: oci.generative_ai_agent_runtime.models.MessageContent
        """
        self._content = content

    @property
    def time_created(self):
        """
        Gets the time_created of this Message.
        The date and time that the message was created in the format of an RFC3339 datetime string.


        :return: The time_created of this Message.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Message.
        The date and time that the message was created in the format of an RFC3339 datetime string.


        :param time_created: The time_created of this Message.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other