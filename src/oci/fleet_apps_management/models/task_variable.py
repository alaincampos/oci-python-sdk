# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskVariable(object):
    """
    The variable of the task.
    At least one of the dynamicArguments or output needs to be provided.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaskVariable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_variables:
            The value to assign to the input_variables property of this TaskVariable.
        :type input_variables: list[oci.fleet_apps_management.models.InputArgument]

        :param output_variables:
            The value to assign to the output_variables property of this TaskVariable.
        :type output_variables: list[str]

        """
        self.swagger_types = {
            'input_variables': 'list[InputArgument]',
            'output_variables': 'list[str]'
        }

        self.attribute_map = {
            'input_variables': 'inputVariables',
            'output_variables': 'outputVariables'
        }

        self._input_variables = None
        self._output_variables = None

    @property
    def input_variables(self):
        """
        Gets the input_variables of this TaskVariable.
        The input variables for the task.


        :return: The input_variables of this TaskVariable.
        :rtype: list[oci.fleet_apps_management.models.InputArgument]
        """
        return self._input_variables

    @input_variables.setter
    def input_variables(self, input_variables):
        """
        Sets the input_variables of this TaskVariable.
        The input variables for the task.


        :param input_variables: The input_variables of this TaskVariable.
        :type: list[oci.fleet_apps_management.models.InputArgument]
        """
        self._input_variables = input_variables

    @property
    def output_variables(self):
        """
        Gets the output_variables of this TaskVariable.
        The list of output variables.


        :return: The output_variables of this TaskVariable.
        :rtype: list[str]
        """
        return self._output_variables

    @output_variables.setter
    def output_variables(self, output_variables):
        """
        Sets the output_variables of this TaskVariable.
        The list of output variables.


        :param output_variables: The output_variables of this TaskVariable.
        :type: list[str]
        """
        self._output_variables = output_variables

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other