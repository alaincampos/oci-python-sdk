# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_details import CreateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOsvcChannelDetails(CreateChannelDetails):
    """
    Properties required to create an OSVC channel.
    """

    #: A constant which can be used with the channel_service property of a CreateOsvcChannelDetails.
    #: This constant has a value of "OSVC"
    CHANNEL_SERVICE_OSVC = "OSVC"

    #: A constant which can be used with the channel_service property of a CreateOsvcChannelDetails.
    #: This constant has a value of "FUSION"
    CHANNEL_SERVICE_FUSION = "FUSION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOsvcChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateOsvcChannelDetails.type` attribute
        of this class is ``OSVC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateOsvcChannelDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateOsvcChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateOsvcChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateOsvcChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOsvcChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOsvcChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param host:
            The value to assign to the host property of this CreateOsvcChannelDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this CreateOsvcChannelDetails.
        :type port: str

        :param user_name:
            The value to assign to the user_name property of this CreateOsvcChannelDetails.
        :type user_name: str

        :param password:
            The value to assign to the password property of this CreateOsvcChannelDetails.
        :type password: str

        :param total_session_count:
            The value to assign to the total_session_count property of this CreateOsvcChannelDetails.
        :type total_session_count: int

        :param channel_service:
            The value to assign to the channel_service property of this CreateOsvcChannelDetails.
            Allowed values for this property are: "OSVC", "FUSION"
        :type channel_service: str

        :param authentication_provider_name:
            The value to assign to the authentication_provider_name property of this CreateOsvcChannelDetails.
        :type authentication_provider_name: str

        :param bot_id:
            The value to assign to the bot_id property of this CreateOsvcChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'host': 'str',
            'port': 'str',
            'user_name': 'str',
            'password': 'str',
            'total_session_count': 'int',
            'channel_service': 'str',
            'authentication_provider_name': 'str',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'host': 'host',
            'port': 'port',
            'user_name': 'userName',
            'password': 'password',
            'total_session_count': 'totalSessionCount',
            'channel_service': 'channelService',
            'authentication_provider_name': 'authenticationProviderName',
            'bot_id': 'botId'
        }

        self._name = None
        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._host = None
        self._port = None
        self._user_name = None
        self._password = None
        self._total_session_count = None
        self._channel_service = None
        self._authentication_provider_name = None
        self._bot_id = None
        self._type = 'OSVC'

    @property
    def host(self):
        """
        **[Required]** Gets the host of this CreateOsvcChannelDetails.
        The host.

        For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface
        or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch,
        then the host is sitename.exampledomain.com.

        For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL.
        For example: sitename.exampledomain.com.


        :return: The host of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this CreateOsvcChannelDetails.
        The host.

        For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface
        or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch,
        then the host is sitename.exampledomain.com.

        For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL.
        For example: sitename.exampledomain.com.


        :param host: The host of this CreateOsvcChannelDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this CreateOsvcChannelDetails.
        The port.


        :return: The port of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateOsvcChannelDetails.
        The port.


        :param port: The port of this CreateOsvcChannelDetails.
        :type: str
        """
        self._port = port

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this CreateOsvcChannelDetails.
        The user name for the digital-assistant agent.


        :return: The user_name of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this CreateOsvcChannelDetails.
        The user name for the digital-assistant agent.


        :param user_name: The user_name of this CreateOsvcChannelDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateOsvcChannelDetails.
        The password for the digital-assistant agent.


        :return: The password of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateOsvcChannelDetails.
        The password for the digital-assistant agent.


        :param password: The password of this CreateOsvcChannelDetails.
        :type: str
        """
        self._password = password

    @property
    def total_session_count(self):
        """
        **[Required]** Gets the total_session_count of this CreateOsvcChannelDetails.
        The total session count.


        :return: The total_session_count of this CreateOsvcChannelDetails.
        :rtype: int
        """
        return self._total_session_count

    @total_session_count.setter
    def total_session_count(self, total_session_count):
        """
        Sets the total_session_count of this CreateOsvcChannelDetails.
        The total session count.


        :param total_session_count: The total_session_count of this CreateOsvcChannelDetails.
        :type: int
        """
        self._total_session_count = total_session_count

    @property
    def channel_service(self):
        """
        Gets the channel_service of this CreateOsvcChannelDetails.
        The type of OSVC service.

        Allowed values for this property are: "OSVC", "FUSION"


        :return: The channel_service of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._channel_service

    @channel_service.setter
    def channel_service(self, channel_service):
        """
        Sets the channel_service of this CreateOsvcChannelDetails.
        The type of OSVC service.


        :param channel_service: The channel_service of this CreateOsvcChannelDetails.
        :type: str
        """
        allowed_values = ["OSVC", "FUSION"]
        if not value_allowed_none_or_none_sentinel(channel_service, allowed_values):
            raise ValueError(
                "Invalid value for `channel_service`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._channel_service = channel_service

    @property
    def authentication_provider_name(self):
        """
        **[Required]** Gets the authentication_provider_name of this CreateOsvcChannelDetails.
        The name of the Authentication Provider to use to authenticate the user.


        :return: The authentication_provider_name of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._authentication_provider_name

    @authentication_provider_name.setter
    def authentication_provider_name(self, authentication_provider_name):
        """
        Sets the authentication_provider_name of this CreateOsvcChannelDetails.
        The name of the Authentication Provider to use to authenticate the user.


        :param authentication_provider_name: The authentication_provider_name of this CreateOsvcChannelDetails.
        :type: str
        """
        self._authentication_provider_name = authentication_provider_name

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateOsvcChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateOsvcChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateOsvcChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateOsvcChannelDetails.
        :type: str
        """
        self._bot_id = bot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other