# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_details import CreateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSlackChannelDetails(CreateChannelDetails):
    """
    Properties required to create a Slack channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSlackChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateSlackChannelDetails.type` attribute
        of this class is ``SLACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateSlackChannelDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateSlackChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateSlackChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateSlackChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSlackChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSlackChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param client_id:
            The value to assign to the client_id property of this CreateSlackChannelDetails.
        :type client_id: str

        :param auth_success_url:
            The value to assign to the auth_success_url property of this CreateSlackChannelDetails.
        :type auth_success_url: str

        :param auth_error_url:
            The value to assign to the auth_error_url property of this CreateSlackChannelDetails.
        :type auth_error_url: str

        :param signing_secret:
            The value to assign to the signing_secret property of this CreateSlackChannelDetails.
        :type signing_secret: str

        :param client_secret:
            The value to assign to the client_secret property of this CreateSlackChannelDetails.
        :type client_secret: str

        :param bot_id:
            The value to assign to the bot_id property of this CreateSlackChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'client_id': 'str',
            'auth_success_url': 'str',
            'auth_error_url': 'str',
            'signing_secret': 'str',
            'client_secret': 'str',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'client_id': 'clientId',
            'auth_success_url': 'authSuccessUrl',
            'auth_error_url': 'authErrorUrl',
            'signing_secret': 'signingSecret',
            'client_secret': 'clientSecret',
            'bot_id': 'botId'
        }

        self._name = None
        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._client_id = None
        self._auth_success_url = None
        self._auth_error_url = None
        self._signing_secret = None
        self._client_secret = None
        self._bot_id = None
        self._type = 'SLACK'

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this CreateSlackChannelDetails.
        The Slack Client Id for the Slack app.


        :return: The client_id of this CreateSlackChannelDetails.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CreateSlackChannelDetails.
        The Slack Client Id for the Slack app.


        :param client_id: The client_id of this CreateSlackChannelDetails.
        :type: str
        """
        self._client_id = client_id

    @property
    def auth_success_url(self):
        """
        Gets the auth_success_url of this CreateSlackChannelDetails.
        The URL to redirect to when authentication is successful.


        :return: The auth_success_url of this CreateSlackChannelDetails.
        :rtype: str
        """
        return self._auth_success_url

    @auth_success_url.setter
    def auth_success_url(self, auth_success_url):
        """
        Sets the auth_success_url of this CreateSlackChannelDetails.
        The URL to redirect to when authentication is successful.


        :param auth_success_url: The auth_success_url of this CreateSlackChannelDetails.
        :type: str
        """
        self._auth_success_url = auth_success_url

    @property
    def auth_error_url(self):
        """
        Gets the auth_error_url of this CreateSlackChannelDetails.
        The URL to redirect to when authentication is unsuccessful.


        :return: The auth_error_url of this CreateSlackChannelDetails.
        :rtype: str
        """
        return self._auth_error_url

    @auth_error_url.setter
    def auth_error_url(self, auth_error_url):
        """
        Sets the auth_error_url of this CreateSlackChannelDetails.
        The URL to redirect to when authentication is unsuccessful.


        :param auth_error_url: The auth_error_url of this CreateSlackChannelDetails.
        :type: str
        """
        self._auth_error_url = auth_error_url

    @property
    def signing_secret(self):
        """
        **[Required]** Gets the signing_secret of this CreateSlackChannelDetails.
        The Signing Secret for the Slack App.


        :return: The signing_secret of this CreateSlackChannelDetails.
        :rtype: str
        """
        return self._signing_secret

    @signing_secret.setter
    def signing_secret(self, signing_secret):
        """
        Sets the signing_secret of this CreateSlackChannelDetails.
        The Signing Secret for the Slack App.


        :param signing_secret: The signing_secret of this CreateSlackChannelDetails.
        :type: str
        """
        self._signing_secret = signing_secret

    @property
    def client_secret(self):
        """
        **[Required]** Gets the client_secret of this CreateSlackChannelDetails.
        The Client Secret for the Slack App.


        :return: The client_secret of this CreateSlackChannelDetails.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this CreateSlackChannelDetails.
        The Client Secret for the Slack App.


        :param client_secret: The client_secret of this CreateSlackChannelDetails.
        :type: str
        """
        self._client_secret = client_secret

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateSlackChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateSlackChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateSlackChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateSlackChannelDetails.
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