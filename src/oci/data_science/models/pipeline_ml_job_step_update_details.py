# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .pipeline_step_update_details import PipelineStepUpdateDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineMLJobStepUpdateDetails(PipelineStepUpdateDetails):
    """
    The type of step where the job is pre-created by the user.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineMLJobStepUpdateDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.PipelineMLJobStepUpdateDetails.step_type` attribute
        of this class is ``ML_JOB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this PipelineMLJobStepUpdateDetails.
            Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT"
        :type step_type: str

        :param step_name:
            The value to assign to the step_name property of this PipelineMLJobStepUpdateDetails.
        :type step_name: str

        :param description:
            The value to assign to the description property of this PipelineMLJobStepUpdateDetails.
        :type description: str

        :param step_configuration_details:
            The value to assign to the step_configuration_details property of this PipelineMLJobStepUpdateDetails.
        :type step_configuration_details: oci.data_science.models.PipelineStepConfigurationDetails

        """
        self.swagger_types = {
            'step_type': 'str',
            'step_name': 'str',
            'description': 'str',
            'step_configuration_details': 'PipelineStepConfigurationDetails'
        }

        self.attribute_map = {
            'step_type': 'stepType',
            'step_name': 'stepName',
            'description': 'description',
            'step_configuration_details': 'stepConfigurationDetails'
        }

        self._step_type = None
        self._step_name = None
        self._description = None
        self._step_configuration_details = None
        self._step_type = 'ML_JOB'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other