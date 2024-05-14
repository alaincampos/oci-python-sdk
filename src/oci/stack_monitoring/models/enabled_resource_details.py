# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnabledResourceDetails(object):
    """
    Details of a resource on which Metric Extension is enabled
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnabledResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this EnabledResourceDetails.
        :type resource_id: str

        """
        self.swagger_types = {
            'resource_id': 'str'
        }

        self.attribute_map = {
            'resource_id': 'resourceId'
        }

        self._resource_id = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this EnabledResourceDetails.
        The OCID of the resource on which Metric Extension is enabled


        :return: The resource_id of this EnabledResourceDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this EnabledResourceDetails.
        The OCID of the resource on which Metric Extension is enabled


        :param resource_id: The resource_id of this EnabledResourceDetails.
        :type: str
        """
        self._resource_id = resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other