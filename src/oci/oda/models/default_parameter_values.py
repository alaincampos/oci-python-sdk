# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultParameterValues(object):
    """
    Default values for parameters required to import a package
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultParameterValues object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_types_default_parameter_values:
            The value to assign to the resource_types_default_parameter_values property of this DefaultParameterValues.
        :type resource_types_default_parameter_values: list[oci.oda.models.ResourceTypeDefaultParameterValues]

        """
        self.swagger_types = {
            'resource_types_default_parameter_values': 'list[ResourceTypeDefaultParameterValues]'
        }

        self.attribute_map = {
            'resource_types_default_parameter_values': 'resourceTypesDefaultParameterValues'
        }

        self._resource_types_default_parameter_values = None

    @property
    def resource_types_default_parameter_values(self):
        """
        Gets the resource_types_default_parameter_values of this DefaultParameterValues.
        A list of resource type specific default parameter values, one set for each resource type listed in the package definition.


        :return: The resource_types_default_parameter_values of this DefaultParameterValues.
        :rtype: list[oci.oda.models.ResourceTypeDefaultParameterValues]
        """
        return self._resource_types_default_parameter_values

    @resource_types_default_parameter_values.setter
    def resource_types_default_parameter_values(self, resource_types_default_parameter_values):
        """
        Sets the resource_types_default_parameter_values of this DefaultParameterValues.
        A list of resource type specific default parameter values, one set for each resource type listed in the package definition.


        :param resource_types_default_parameter_values: The resource_types_default_parameter_values of this DefaultParameterValues.
        :type: list[oci.oda.models.ResourceTypeDefaultParameterValues]
        """
        self._resource_types_default_parameter_values = resource_types_default_parameter_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other