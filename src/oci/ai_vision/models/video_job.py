# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoJob(object):
    """
    Job details for a video analysis.
    """

    #: A constant which can be used with the lifecycle_state property of a VideoJob.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a VideoJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a VideoJob.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a VideoJob.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a VideoJob.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a VideoJob.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_details property of a VideoJob.
    #: This constant has a value of "PARTIALLY_SUCCEEDED"
    LIFECYCLE_DETAILS_PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"

    #: A constant which can be used with the lifecycle_details property of a VideoJob.
    #: This constant has a value of "COMPLETELY_FAILED"
    LIFECYCLE_DETAILS_COMPLETELY_FAILED = "COMPLETELY_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new VideoJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VideoJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VideoJob.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VideoJob.
        :type display_name: str

        :param features:
            The value to assign to the features property of this VideoJob.
        :type features: list[oci.ai_vision.models.VideoFeature]

        :param input_location:
            The value to assign to the input_location property of this VideoJob.
        :type input_location: oci.ai_vision.models.InputLocation

        :param time_accepted:
            The value to assign to the time_accepted property of this VideoJob.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this VideoJob.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this VideoJob.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this VideoJob.
        :type percent_complete: float

        :param output_location:
            The value to assign to the output_location property of this VideoJob.
        :type output_location: oci.ai_vision.models.OutputLocation

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VideoJob.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VideoJob.
            Allowed values for this property are: "PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VideoJob.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VideoJob.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VideoJob.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'features': 'list[VideoFeature]',
            'input_location': 'InputLocation',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'float',
            'output_location': 'OutputLocation',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'features': 'features',
            'input_location': 'inputLocation',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete',
            'output_location': 'outputLocation',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._features = None
        self._input_location = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._percent_complete = None
        self._output_location = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VideoJob.
        Id of the job.


        :return: The id of this VideoJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VideoJob.
        Id of the job.


        :param id: The id of this VideoJob.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VideoJob.
        The ocid of the compartment that starts the job.


        :return: The compartment_id of this VideoJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VideoJob.
        The ocid of the compartment that starts the job.


        :param compartment_id: The compartment_id of this VideoJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VideoJob.
        Video job display name.


        :return: The display_name of this VideoJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VideoJob.
        Video job display name.


        :param display_name: The display_name of this VideoJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def features(self):
        """
        **[Required]** Gets the features of this VideoJob.
        a list of document analysis features.


        :return: The features of this VideoJob.
        :rtype: list[oci.ai_vision.models.VideoFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this VideoJob.
        a list of document analysis features.


        :param features: The features of this VideoJob.
        :type: list[oci.ai_vision.models.VideoFeature]
        """
        self._features = features

    @property
    def input_location(self):
        """
        Gets the input_location of this VideoJob.

        :return: The input_location of this VideoJob.
        :rtype: oci.ai_vision.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this VideoJob.

        :param input_location: The input_location of this VideoJob.
        :type: oci.ai_vision.models.InputLocation
        """
        self._input_location = input_location

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this VideoJob.
        Job accepted time.


        :return: The time_accepted of this VideoJob.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this VideoJob.
        Job accepted time.


        :param time_accepted: The time_accepted of this VideoJob.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this VideoJob.
        Job started time.


        :return: The time_started of this VideoJob.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this VideoJob.
        Job started time.


        :param time_started: The time_started of this VideoJob.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this VideoJob.
        Job finished time.


        :return: The time_finished of this VideoJob.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this VideoJob.
        Job finished time.


        :param time_finished: The time_finished of this VideoJob.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this VideoJob.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :return: The percent_complete of this VideoJob.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this VideoJob.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :param percent_complete: The percent_complete of this VideoJob.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this VideoJob.

        :return: The output_location of this VideoJob.
        :rtype: oci.ai_vision.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this VideoJob.

        :param output_location: The output_location of this VideoJob.
        :type: oci.ai_vision.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VideoJob.
        The current state of the batch document job.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VideoJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VideoJob.
        The current state of the batch document job.


        :param lifecycle_state: The lifecycle_state of this VideoJob.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this VideoJob.
        Detailed status of FAILED state.

        Allowed values for this property are: "PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this VideoJob.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this VideoJob.
        Detailed status of FAILED state.


        :param lifecycle_details: The lifecycle_details of this VideoJob.
        :type: str
        """
        allowed_values = ["PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VideoJob.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this VideoJob.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VideoJob.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this VideoJob.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VideoJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this VideoJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VideoJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this VideoJob.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this VideoJob.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this VideoJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this VideoJob.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this VideoJob.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other