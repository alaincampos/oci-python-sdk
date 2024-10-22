# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericArtifact(object):
    """
    Patch artifact metadata Details which is common for all platforms.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericArtifact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content:
            The value to assign to the content property of this GenericArtifact.
        :type content: oci.fleet_apps_management.models.ContentDetails

        """
        self.swagger_types = {
            'content': 'ContentDetails'
        }

        self.attribute_map = {
            'content': 'content'
        }

        self._content = None

    @property
    def content(self):
        """
        **[Required]** Gets the content of this GenericArtifact.

        :return: The content of this GenericArtifact.
        :rtype: oci.fleet_apps_management.models.ContentDetails
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this GenericArtifact.

        :param content: The content of this GenericArtifact.
        :type: oci.fleet_apps_management.models.ContentDetails
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
