# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmbedTextDetails(object):
    """
    Details for the request to embed texts.
    """

    #: A constant which can be used with the truncate property of a EmbedTextDetails.
    #: This constant has a value of "NONE"
    TRUNCATE_NONE = "NONE"

    #: A constant which can be used with the truncate property of a EmbedTextDetails.
    #: This constant has a value of "START"
    TRUNCATE_START = "START"

    #: A constant which can be used with the truncate property of a EmbedTextDetails.
    #: This constant has a value of "END"
    TRUNCATE_END = "END"

    #: A constant which can be used with the input_type property of a EmbedTextDetails.
    #: This constant has a value of "SEARCH_DOCUMENT"
    INPUT_TYPE_SEARCH_DOCUMENT = "SEARCH_DOCUMENT"

    #: A constant which can be used with the input_type property of a EmbedTextDetails.
    #: This constant has a value of "SEARCH_QUERY"
    INPUT_TYPE_SEARCH_QUERY = "SEARCH_QUERY"

    #: A constant which can be used with the input_type property of a EmbedTextDetails.
    #: This constant has a value of "CLASSIFICATION"
    INPUT_TYPE_CLASSIFICATION = "CLASSIFICATION"

    #: A constant which can be used with the input_type property of a EmbedTextDetails.
    #: This constant has a value of "CLUSTERING"
    INPUT_TYPE_CLUSTERING = "CLUSTERING"

    def __init__(self, **kwargs):
        """
        Initializes a new EmbedTextDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param inputs:
            The value to assign to the inputs property of this EmbedTextDetails.
        :type inputs: list[str]

        :param serving_mode:
            The value to assign to the serving_mode property of this EmbedTextDetails.
        :type serving_mode: oci.generative_ai_inference.models.ServingMode

        :param compartment_id:
            The value to assign to the compartment_id property of this EmbedTextDetails.
        :type compartment_id: str

        :param is_echo:
            The value to assign to the is_echo property of this EmbedTextDetails.
        :type is_echo: bool

        :param truncate:
            The value to assign to the truncate property of this EmbedTextDetails.
            Allowed values for this property are: "NONE", "START", "END"
        :type truncate: str

        :param input_type:
            The value to assign to the input_type property of this EmbedTextDetails.
            Allowed values for this property are: "SEARCH_DOCUMENT", "SEARCH_QUERY", "CLASSIFICATION", "CLUSTERING"
        :type input_type: str

        """
        self.swagger_types = {
            'inputs': 'list[str]',
            'serving_mode': 'ServingMode',
            'compartment_id': 'str',
            'is_echo': 'bool',
            'truncate': 'str',
            'input_type': 'str'
        }

        self.attribute_map = {
            'inputs': 'inputs',
            'serving_mode': 'servingMode',
            'compartment_id': 'compartmentId',
            'is_echo': 'isEcho',
            'truncate': 'truncate',
            'input_type': 'inputType'
        }

        self._inputs = None
        self._serving_mode = None
        self._compartment_id = None
        self._is_echo = None
        self._truncate = None
        self._input_type = None

    @property
    def inputs(self):
        """
        **[Required]** Gets the inputs of this EmbedTextDetails.
        Provide a list of strings with a maximum number of 96 entries. Each string can be words, a phrase, or a paragraph. The maximum length of each string entry in the list is 512 tokens.


        :return: The inputs of this EmbedTextDetails.
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this EmbedTextDetails.
        Provide a list of strings with a maximum number of 96 entries. Each string can be words, a phrase, or a paragraph. The maximum length of each string entry in the list is 512 tokens.


        :param inputs: The inputs of this EmbedTextDetails.
        :type: list[str]
        """
        self._inputs = inputs

    @property
    def serving_mode(self):
        """
        **[Required]** Gets the serving_mode of this EmbedTextDetails.

        :return: The serving_mode of this EmbedTextDetails.
        :rtype: oci.generative_ai_inference.models.ServingMode
        """
        return self._serving_mode

    @serving_mode.setter
    def serving_mode(self, serving_mode):
        """
        Sets the serving_mode of this EmbedTextDetails.

        :param serving_mode: The serving_mode of this EmbedTextDetails.
        :type: oci.generative_ai_inference.models.ServingMode
        """
        self._serving_mode = serving_mode

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EmbedTextDetails.
        The OCID of compartment that the user is authorized to use to call into the Generative AI service.


        :return: The compartment_id of this EmbedTextDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EmbedTextDetails.
        The OCID of compartment that the user is authorized to use to call into the Generative AI service.


        :param compartment_id: The compartment_id of this EmbedTextDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_echo(self):
        """
        Gets the is_echo of this EmbedTextDetails.
        Whether or not to include the original inputs in the response. Results are index-based.


        :return: The is_echo of this EmbedTextDetails.
        :rtype: bool
        """
        return self._is_echo

    @is_echo.setter
    def is_echo(self, is_echo):
        """
        Sets the is_echo of this EmbedTextDetails.
        Whether or not to include the original inputs in the response. Results are index-based.


        :param is_echo: The is_echo of this EmbedTextDetails.
        :type: bool
        """
        self._is_echo = is_echo

    @property
    def truncate(self):
        """
        Gets the truncate of this EmbedTextDetails.
        For an input that's longer than the maximum token length, specifies which part of the input text will be truncated.

        Allowed values for this property are: "NONE", "START", "END"


        :return: The truncate of this EmbedTextDetails.
        :rtype: str
        """
        return self._truncate

    @truncate.setter
    def truncate(self, truncate):
        """
        Sets the truncate of this EmbedTextDetails.
        For an input that's longer than the maximum token length, specifies which part of the input text will be truncated.


        :param truncate: The truncate of this EmbedTextDetails.
        :type: str
        """
        allowed_values = ["NONE", "START", "END"]
        if not value_allowed_none_or_none_sentinel(truncate, allowed_values):
            raise ValueError(
                f"Invalid value for `truncate`, must be None or one of {allowed_values}"
            )
        self._truncate = truncate

    @property
    def input_type(self):
        """
        Gets the input_type of this EmbedTextDetails.
        Specifies the input type.

        Allowed values for this property are: "SEARCH_DOCUMENT", "SEARCH_QUERY", "CLASSIFICATION", "CLUSTERING"


        :return: The input_type of this EmbedTextDetails.
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """
        Sets the input_type of this EmbedTextDetails.
        Specifies the input type.


        :param input_type: The input_type of this EmbedTextDetails.
        :type: str
        """
        allowed_values = ["SEARCH_DOCUMENT", "SEARCH_QUERY", "CLASSIFICATION", "CLUSTERING"]
        if not value_allowed_none_or_none_sentinel(input_type, allowed_values):
            raise ValueError(
                f"Invalid value for `input_type`, must be None or one of {allowed_values}"
            )
        self._input_type = input_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other