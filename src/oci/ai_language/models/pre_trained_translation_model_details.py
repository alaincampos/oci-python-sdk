# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001

from .model_details import ModelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreTrainedTranslationModelDetails(ModelDetails):
    """
    Possible pre trained translation model information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PreTrainedTranslationModelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.PreTrainedTranslationModelDetails.model_type` attribute
        of this class is ``PRE_TRAINED_TRANSLATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param language_code:
            The value to assign to the language_code property of this PreTrainedTranslationModelDetails.
        :type language_code: str

        :param model_type:
            The value to assign to the model_type property of this PreTrainedTranslationModelDetails.
            Allowed values for this property are: "NAMED_ENTITY_RECOGNITION", "TEXT_CLASSIFICATION", "PRE_TRAINED_NAMED_ENTITY_RECOGNITION", "PRE_TRAINED_TEXT_CLASSIFICATION", "PRE_TRAINED_SENTIMENT_ANALYSIS", "PRE_TRAINED_KEYPHRASE_EXTRACTION", "PRE_TRAINED_LANGUAGE_DETECTION", "PRE_TRAINED_PII", "PRE_TRAINED_HEALTH_NLU", "PRE_TRAINED_SUMMARIZATION", "PRE_TRAINED_UNIVERSAL", "PII", "PRE_TRAINED_TRANSLATION", "HEALTH_NLU"
        :type model_type: str

        :param version:
            The value to assign to the version property of this PreTrainedTranslationModelDetails.
        :type version: str

        """
        self.swagger_types = {
            'language_code': 'str',
            'model_type': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'language_code': 'languageCode',
            'model_type': 'modelType',
            'version': 'version'
        }

        self._language_code = None
        self._model_type = None
        self._version = None
        self._model_type = 'PRE_TRAINED_TRANSLATION'

    @property
    def version(self):
        """
        Gets the version of this PreTrainedTranslationModelDetails.
        Optional pre trained model version. If nothing specified latest pre trained model will be used.
        Supported versions can be found at /modelTypes/{modelType}


        :return: The version of this PreTrainedTranslationModelDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PreTrainedTranslationModelDetails.
        Optional pre trained model version. If nothing specified latest pre trained model will be used.
        Supported versions can be found at /modelTypes/{modelType}


        :param version: The version of this PreTrainedTranslationModelDetails.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other