# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_channel_details import UpdateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAppEventChannelDetails(UpdateChannelDetails):
    """
    Properties to update an Application Event channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAppEventChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.UpdateAppEventChannelDetails.type` attribute
        of this class is ``APPEVENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateAppEventChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this UpdateAppEventChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this UpdateAppEventChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAppEventChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAppEventChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param outbound_url:
            The value to assign to the outbound_url property of this UpdateAppEventChannelDetails.
        :type outbound_url: str

        :param event_sink_bot_ids:
            The value to assign to the event_sink_bot_ids property of this UpdateAppEventChannelDetails.
        :type event_sink_bot_ids: list[str]

        """
        self.swagger_types = {
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'outbound_url': 'str',
            'event_sink_bot_ids': 'list[str]'
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'outbound_url': 'outboundUrl',
            'event_sink_bot_ids': 'eventSinkBotIds'
        }

        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._outbound_url = None
        self._event_sink_bot_ids = None
        self._type = 'APPEVENT'

    @property
    def outbound_url(self):
        """
        Gets the outbound_url of this UpdateAppEventChannelDetails.
        The URL for sending errors and responses to.


        :return: The outbound_url of this UpdateAppEventChannelDetails.
        :rtype: str
        """
        return self._outbound_url

    @outbound_url.setter
    def outbound_url(self, outbound_url):
        """
        Sets the outbound_url of this UpdateAppEventChannelDetails.
        The URL for sending errors and responses to.


        :param outbound_url: The outbound_url of this UpdateAppEventChannelDetails.
        :type: str
        """
        self._outbound_url = outbound_url

    @property
    def event_sink_bot_ids(self):
        """
        Gets the event_sink_bot_ids of this UpdateAppEventChannelDetails.
        The IDs of the Skills and Digital Assistants that the Channel is routed to.


        :return: The event_sink_bot_ids of this UpdateAppEventChannelDetails.
        :rtype: list[str]
        """
        return self._event_sink_bot_ids

    @event_sink_bot_ids.setter
    def event_sink_bot_ids(self, event_sink_bot_ids):
        """
        Sets the event_sink_bot_ids of this UpdateAppEventChannelDetails.
        The IDs of the Skills and Digital Assistants that the Channel is routed to.


        :param event_sink_bot_ids: The event_sink_bot_ids of this UpdateAppEventChannelDetails.
        :type: list[str]
        """
        self._event_sink_bot_ids = event_sink_bot_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other