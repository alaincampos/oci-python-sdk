# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Citation(object):
    """
    A section of the generated reply which cites external knowledge.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Citation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start:
            The value to assign to the start property of this Citation.
        :type start: int

        :param end:
            The value to assign to the end property of this Citation.
        :type end: int

        :param text:
            The value to assign to the text property of this Citation.
        :type text: str

        :param document_ids:
            The value to assign to the document_ids property of this Citation.
        :type document_ids: list[str]

        """
        self.swagger_types = {
            'start': 'int',
            'end': 'int',
            'text': 'str',
            'document_ids': 'list[str]'
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end',
            'text': 'text',
            'document_ids': 'documentIds'
        }

        self._start = None
        self._end = None
        self._text = None
        self._document_ids = None

    @property
    def start(self):
        """
        **[Required]** Gets the start of this Citation.
        The index of text that the citation starts at, counting from zero.


        :return: The start of this Citation.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this Citation.
        The index of text that the citation starts at, counting from zero.


        :param start: The start of this Citation.
        :type: int
        """
        self._start = start

    @property
    def end(self):
        """
        **[Required]** Gets the end of this Citation.
        The index of text that the citation ends after, counting from zero.


        :return: The end of this Citation.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this Citation.
        The index of text that the citation ends after, counting from zero.


        :param end: The end of this Citation.
        :type: int
        """
        self._end = end

    @property
    def text(self):
        """
        **[Required]** Gets the text of this Citation.
        The text of the citation


        :return: The text of this Citation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Citation.
        The text of the citation


        :param text: The text of this Citation.
        :type: str
        """
        self._text = text

    @property
    def document_ids(self):
        """
        **[Required]** Gets the document_ids of this Citation.
        Identifiers of documents cited by this section of the generated reply.


        :return: The document_ids of this Citation.
        :rtype: list[str]
        """
        return self._document_ids

    @document_ids.setter
    def document_ids(self, document_ids):
        """
        Sets the document_ids of this Citation.
        Identifiers of documents cited by this section of the generated reply.


        :param document_ids: The document_ids of this Citation.
        :type: list[str]
        """
        self._document_ids = document_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other