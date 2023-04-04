# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStreamCdnConfigDetails(object):
    """
    The information about the new CDN Configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStreamCdnConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateStreamCdnConfigDetails.
        :type display_name: str

        :param distribution_channel_id:
            The value to assign to the distribution_channel_id property of this CreateStreamCdnConfigDetails.
        :type distribution_channel_id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateStreamCdnConfigDetails.
        :type is_enabled: bool

        :param config:
            The value to assign to the config property of this CreateStreamCdnConfigDetails.
        :type config: oci.media_services.models.StreamCdnConfigSection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateStreamCdnConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateStreamCdnConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'distribution_channel_id': 'str',
            'is_enabled': 'bool',
            'config': 'StreamCdnConfigSection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'distribution_channel_id': 'distributionChannelId',
            'is_enabled': 'isEnabled',
            'config': 'config',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._distribution_channel_id = None
        self._is_enabled = None
        self._config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateStreamCdnConfigDetails.
        CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this CreateStreamCdnConfigDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateStreamCdnConfigDetails.
        CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreateStreamCdnConfigDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def distribution_channel_id(self):
        """
        **[Required]** Gets the distribution_channel_id of this CreateStreamCdnConfigDetails.
        Distribution Channel Identifier.


        :return: The distribution_channel_id of this CreateStreamCdnConfigDetails.
        :rtype: str
        """
        return self._distribution_channel_id

    @distribution_channel_id.setter
    def distribution_channel_id(self, distribution_channel_id):
        """
        Sets the distribution_channel_id of this CreateStreamCdnConfigDetails.
        Distribution Channel Identifier.


        :param distribution_channel_id: The distribution_channel_id of this CreateStreamCdnConfigDetails.
        :type: str
        """
        self._distribution_channel_id = distribution_channel_id

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateStreamCdnConfigDetails.
        Whether publishing to CDN is enabled.


        :return: The is_enabled of this CreateStreamCdnConfigDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateStreamCdnConfigDetails.
        Whether publishing to CDN is enabled.


        :param is_enabled: The is_enabled of this CreateStreamCdnConfigDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def config(self):
        """
        **[Required]** Gets the config of this CreateStreamCdnConfigDetails.

        :return: The config of this CreateStreamCdnConfigDetails.
        :rtype: oci.media_services.models.StreamCdnConfigSection
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this CreateStreamCdnConfigDetails.

        :param config: The config of this CreateStreamCdnConfigDetails.
        :type: oci.media_services.models.StreamCdnConfigSection
        """
        self._config = config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateStreamCdnConfigDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateStreamCdnConfigDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateStreamCdnConfigDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateStreamCdnConfigDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateStreamCdnConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateStreamCdnConfigDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateStreamCdnConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateStreamCdnConfigDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other