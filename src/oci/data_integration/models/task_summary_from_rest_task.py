# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .task_summary import TaskSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskSummaryFromRestTask(TaskSummary):
    """
    The information about the Generic REST task.
    """

    #: A constant which can be used with the method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "GET"
    METHOD_TYPE_GET = "GET"

    #: A constant which can be used with the method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "POST"
    METHOD_TYPE_POST = "POST"

    #: A constant which can be used with the method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "PATCH"
    METHOD_TYPE_PATCH = "PATCH"

    #: A constant which can be used with the method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "DELETE"
    METHOD_TYPE_DELETE = "DELETE"

    #: A constant which can be used with the method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "PUT"
    METHOD_TYPE_PUT = "PUT"

    #: A constant which can be used with the api_call_mode property of a TaskSummaryFromRestTask.
    #: This constant has a value of "SYNCHRONOUS"
    API_CALL_MODE_SYNCHRONOUS = "SYNCHRONOUS"

    #: A constant which can be used with the api_call_mode property of a TaskSummaryFromRestTask.
    #: This constant has a value of "ASYNC_OCI_WORKREQUEST"
    API_CALL_MODE_ASYNC_OCI_WORKREQUEST = "ASYNC_OCI_WORKREQUEST"

    #: A constant which can be used with the cancel_method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "GET"
    CANCEL_METHOD_TYPE_GET = "GET"

    #: A constant which can be used with the cancel_method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "POST"
    CANCEL_METHOD_TYPE_POST = "POST"

    #: A constant which can be used with the cancel_method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "PATCH"
    CANCEL_METHOD_TYPE_PATCH = "PATCH"

    #: A constant which can be used with the cancel_method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "DELETE"
    CANCEL_METHOD_TYPE_DELETE = "DELETE"

    #: A constant which can be used with the cancel_method_type property of a TaskSummaryFromRestTask.
    #: This constant has a value of "PUT"
    CANCEL_METHOD_TYPE_PUT = "PUT"

    def __init__(self, **kwargs):
        """
        Initializes a new TaskSummaryFromRestTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.TaskSummaryFromRestTask.model_type` attribute
        of this class is ``REST_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TaskSummaryFromRestTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this TaskSummaryFromRestTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TaskSummaryFromRestTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskSummaryFromRestTask.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskSummaryFromRestTask.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskSummaryFromRestTask.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskSummaryFromRestTask.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this TaskSummaryFromRestTask.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TaskSummaryFromRestTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this TaskSummaryFromRestTask.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this TaskSummaryFromRestTask.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this TaskSummaryFromRestTask.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this TaskSummaryFromRestTask.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this TaskSummaryFromRestTask.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param metadata:
            The value to assign to the metadata property of this TaskSummaryFromRestTask.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this TaskSummaryFromRestTask.
        :type key_map: dict(str, str)

        :param auth_details:
            The value to assign to the auth_details property of this TaskSummaryFromRestTask.
        :type auth_details: oci.data_integration.models.AuthDetails

        :param endpoint:
            The value to assign to the endpoint property of this TaskSummaryFromRestTask.
        :type endpoint: oci.data_integration.models.Expression

        :param method_type:
            The value to assign to the method_type property of this TaskSummaryFromRestTask.
            Allowed values for this property are: "GET", "POST", "PATCH", "DELETE", "PUT"
        :type method_type: str

        :param headers:
            The value to assign to the headers property of this TaskSummaryFromRestTask.
        :type headers: object

        :param json_data:
            The value to assign to the json_data property of this TaskSummaryFromRestTask.
        :type json_data: str

        :param api_call_mode:
            The value to assign to the api_call_mode property of this TaskSummaryFromRestTask.
            Allowed values for this property are: "SYNCHRONOUS", "ASYNC_OCI_WORKREQUEST"
        :type api_call_mode: str

        :param cancel_endpoint:
            The value to assign to the cancel_endpoint property of this TaskSummaryFromRestTask.
        :type cancel_endpoint: oci.data_integration.models.Expression

        :param cancel_method_type:
            The value to assign to the cancel_method_type property of this TaskSummaryFromRestTask.
            Allowed values for this property are: "GET", "POST", "PATCH", "DELETE", "PUT"
        :type cancel_method_type: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'ConfigProvider',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)',
            'auth_details': 'AuthDetails',
            'endpoint': 'Expression',
            'method_type': 'str',
            'headers': 'object',
            'json_data': 'str',
            'api_call_mode': 'str',
            'cancel_endpoint': 'Expression',
            'cancel_method_type': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'metadata': 'metadata',
            'key_map': 'keyMap',
            'auth_details': 'authDetails',
            'endpoint': 'endpoint',
            'method_type': 'methodType',
            'headers': 'headers',
            'json_data': 'jsonData',
            'api_call_mode': 'apiCallMode',
            'cancel_endpoint': 'cancelEndpoint',
            'cancel_method_type': 'cancelMethodType'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._metadata = None
        self._key_map = None
        self._auth_details = None
        self._endpoint = None
        self._method_type = None
        self._headers = None
        self._json_data = None
        self._api_call_mode = None
        self._cancel_endpoint = None
        self._cancel_method_type = None
        self._model_type = 'REST_TASK'

    @property
    def auth_details(self):
        """
        Gets the auth_details of this TaskSummaryFromRestTask.

        :return: The auth_details of this TaskSummaryFromRestTask.
        :rtype: oci.data_integration.models.AuthDetails
        """
        return self._auth_details

    @auth_details.setter
    def auth_details(self, auth_details):
        """
        Sets the auth_details of this TaskSummaryFromRestTask.

        :param auth_details: The auth_details of this TaskSummaryFromRestTask.
        :type: oci.data_integration.models.AuthDetails
        """
        self._auth_details = auth_details

    @property
    def endpoint(self):
        """
        Gets the endpoint of this TaskSummaryFromRestTask.

        :return: The endpoint of this TaskSummaryFromRestTask.
        :rtype: oci.data_integration.models.Expression
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this TaskSummaryFromRestTask.

        :param endpoint: The endpoint of this TaskSummaryFromRestTask.
        :type: oci.data_integration.models.Expression
        """
        self._endpoint = endpoint

    @property
    def method_type(self):
        """
        Gets the method_type of this TaskSummaryFromRestTask.
        The REST method to use.

        Allowed values for this property are: "GET", "POST", "PATCH", "DELETE", "PUT"


        :return: The method_type of this TaskSummaryFromRestTask.
        :rtype: str
        """
        return self._method_type

    @method_type.setter
    def method_type(self, method_type):
        """
        Sets the method_type of this TaskSummaryFromRestTask.
        The REST method to use.


        :param method_type: The method_type of this TaskSummaryFromRestTask.
        :type: str
        """
        allowed_values = ["GET", "POST", "PATCH", "DELETE", "PUT"]
        if not value_allowed_none_or_none_sentinel(method_type, allowed_values):
            raise ValueError(
                "Invalid value for `method_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._method_type = method_type

    @property
    def headers(self):
        """
        Gets the headers of this TaskSummaryFromRestTask.
        The headers for the REST call.


        :return: The headers of this TaskSummaryFromRestTask.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this TaskSummaryFromRestTask.
        The headers for the REST call.


        :param headers: The headers of this TaskSummaryFromRestTask.
        :type: object
        """
        self._headers = headers

    @property
    def json_data(self):
        """
        Gets the json_data of this TaskSummaryFromRestTask.
        JSON data for payload body.


        :return: The json_data of this TaskSummaryFromRestTask.
        :rtype: str
        """
        return self._json_data

    @json_data.setter
    def json_data(self, json_data):
        """
        Sets the json_data of this TaskSummaryFromRestTask.
        JSON data for payload body.


        :param json_data: The json_data of this TaskSummaryFromRestTask.
        :type: str
        """
        self._json_data = json_data

    @property
    def api_call_mode(self):
        """
        Gets the api_call_mode of this TaskSummaryFromRestTask.
        The invocation type to be used for Generic REST invocation.

        Allowed values for this property are: "SYNCHRONOUS", "ASYNC_OCI_WORKREQUEST"


        :return: The api_call_mode of this TaskSummaryFromRestTask.
        :rtype: str
        """
        return self._api_call_mode

    @api_call_mode.setter
    def api_call_mode(self, api_call_mode):
        """
        Sets the api_call_mode of this TaskSummaryFromRestTask.
        The invocation type to be used for Generic REST invocation.


        :param api_call_mode: The api_call_mode of this TaskSummaryFromRestTask.
        :type: str
        """
        allowed_values = ["SYNCHRONOUS", "ASYNC_OCI_WORKREQUEST"]
        if not value_allowed_none_or_none_sentinel(api_call_mode, allowed_values):
            raise ValueError(
                "Invalid value for `api_call_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._api_call_mode = api_call_mode

    @property
    def cancel_endpoint(self):
        """
        Gets the cancel_endpoint of this TaskSummaryFromRestTask.

        :return: The cancel_endpoint of this TaskSummaryFromRestTask.
        :rtype: oci.data_integration.models.Expression
        """
        return self._cancel_endpoint

    @cancel_endpoint.setter
    def cancel_endpoint(self, cancel_endpoint):
        """
        Sets the cancel_endpoint of this TaskSummaryFromRestTask.

        :param cancel_endpoint: The cancel_endpoint of this TaskSummaryFromRestTask.
        :type: oci.data_integration.models.Expression
        """
        self._cancel_endpoint = cancel_endpoint

    @property
    def cancel_method_type(self):
        """
        Gets the cancel_method_type of this TaskSummaryFromRestTask.
        The REST method to use for canceling the original request.

        Allowed values for this property are: "GET", "POST", "PATCH", "DELETE", "PUT"


        :return: The cancel_method_type of this TaskSummaryFromRestTask.
        :rtype: str
        """
        return self._cancel_method_type

    @cancel_method_type.setter
    def cancel_method_type(self, cancel_method_type):
        """
        Sets the cancel_method_type of this TaskSummaryFromRestTask.
        The REST method to use for canceling the original request.


        :param cancel_method_type: The cancel_method_type of this TaskSummaryFromRestTask.
        :type: str
        """
        allowed_values = ["GET", "POST", "PATCH", "DELETE", "PUT"]
        if not value_allowed_none_or_none_sentinel(cancel_method_type, allowed_values):
            raise ValueError(
                "Invalid value for `cancel_method_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._cancel_method_type = cancel_method_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other