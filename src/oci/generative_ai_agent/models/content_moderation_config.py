# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContentModerationConfig(object):
    """
    The configuration details about whether to apply the content moderation feature to input and output. Content moderation removes toxic and biased content from responses. It is recommended to use content moderation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContentModerationConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param should_enable_on_input:
            The value to assign to the should_enable_on_input property of this ContentModerationConfig.
        :type should_enable_on_input: bool

        :param should_enable_on_output:
            The value to assign to the should_enable_on_output property of this ContentModerationConfig.
        :type should_enable_on_output: bool

        """
        self.swagger_types = {
            'should_enable_on_input': 'bool',
            'should_enable_on_output': 'bool'
        }

        self.attribute_map = {
            'should_enable_on_input': 'shouldEnableOnInput',
            'should_enable_on_output': 'shouldEnableOnOutput'
        }

        self._should_enable_on_input = None
        self._should_enable_on_output = None

    @property
    def should_enable_on_input(self):
        """
        Gets the should_enable_on_input of this ContentModerationConfig.
        A flag to enable or disable content moderation on input.


        :return: The should_enable_on_input of this ContentModerationConfig.
        :rtype: bool
        """
        return self._should_enable_on_input

    @should_enable_on_input.setter
    def should_enable_on_input(self, should_enable_on_input):
        """
        Sets the should_enable_on_input of this ContentModerationConfig.
        A flag to enable or disable content moderation on input.


        :param should_enable_on_input: The should_enable_on_input of this ContentModerationConfig.
        :type: bool
        """
        self._should_enable_on_input = should_enable_on_input

    @property
    def should_enable_on_output(self):
        """
        Gets the should_enable_on_output of this ContentModerationConfig.
        A flag to enable or disable content moderation on output.


        :return: The should_enable_on_output of this ContentModerationConfig.
        :rtype: bool
        """
        return self._should_enable_on_output

    @should_enable_on_output.setter
    def should_enable_on_output(self, should_enable_on_output):
        """
        Sets the should_enable_on_output of this ContentModerationConfig.
        A flag to enable or disable content moderation on output.


        :param should_enable_on_output: The should_enable_on_output of this ContentModerationConfig.
        :type: bool
        """
        self._should_enable_on_output = should_enable_on_output

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other