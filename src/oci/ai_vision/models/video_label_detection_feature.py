# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .video_feature import VideoFeature
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoLabelDetectionFeature(VideoFeature):
    """
    Video label detection feature
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoLabelDetectionFeature object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.VideoLabelDetectionFeature.feature_type` attribute
        of this class is ``LABEL_DETECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this VideoLabelDetectionFeature.
            Allowed values for this property are: "LABEL_DETECTION", "OBJECT_DETECTION", "TEXT_DETECTION", "FACE_DETECTION", "OBJECT_TRACKING"
        :type feature_type: str

        :param min_confidence:
            The value to assign to the min_confidence property of this VideoLabelDetectionFeature.
        :type min_confidence: float

        :param max_results:
            The value to assign to the max_results property of this VideoLabelDetectionFeature.
        :type max_results: int

        :param model_id:
            The value to assign to the model_id property of this VideoLabelDetectionFeature.
        :type model_id: str

        """
        self.swagger_types = {
            'feature_type': 'str',
            'min_confidence': 'float',
            'max_results': 'int',
            'model_id': 'str'
        }

        self.attribute_map = {
            'feature_type': 'featureType',
            'min_confidence': 'minConfidence',
            'max_results': 'maxResults',
            'model_id': 'modelId'
        }

        self._feature_type = None
        self._min_confidence = None
        self._max_results = None
        self._model_id = None
        self._feature_type = 'LABEL_DETECTION'

    @property
    def min_confidence(self):
        """
        Gets the min_confidence of this VideoLabelDetectionFeature.
        The minimum confidence score, between 0 and 1,
        when the value is set, results with lower confidence will not be returned.


        :return: The min_confidence of this VideoLabelDetectionFeature.
        :rtype: float
        """
        return self._min_confidence

    @min_confidence.setter
    def min_confidence(self, min_confidence):
        """
        Sets the min_confidence of this VideoLabelDetectionFeature.
        The minimum confidence score, between 0 and 1,
        when the value is set, results with lower confidence will not be returned.


        :param min_confidence: The min_confidence of this VideoLabelDetectionFeature.
        :type: float
        """
        self._min_confidence = min_confidence

    @property
    def max_results(self):
        """
        Gets the max_results of this VideoLabelDetectionFeature.
        The maximum number of results per video frame to return.


        :return: The max_results of this VideoLabelDetectionFeature.
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """
        Sets the max_results of this VideoLabelDetectionFeature.
        The maximum number of results per video frame to return.


        :param max_results: The max_results of this VideoLabelDetectionFeature.
        :type: int
        """
        self._max_results = max_results

    @property
    def model_id(self):
        """
        Gets the model_id of this VideoLabelDetectionFeature.
        The custom model ID.


        :return: The model_id of this VideoLabelDetectionFeature.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this VideoLabelDetectionFeature.
        The custom model ID.


        :param model_id: The model_id of this VideoLabelDetectionFeature.
        :type: str
        """
        self._model_id = model_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other