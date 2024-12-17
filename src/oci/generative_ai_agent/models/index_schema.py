# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndexSchema(object):
    """
    The index schema details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IndexSchema object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param body_key:
            The value to assign to the body_key property of this IndexSchema.
        :type body_key: str

        :param url_key:
            The value to assign to the url_key property of this IndexSchema.
        :type url_key: str

        :param title_key:
            The value to assign to the title_key property of this IndexSchema.
        :type title_key: str

        :param embedding_body_key:
            The value to assign to the embedding_body_key property of this IndexSchema.
        :type embedding_body_key: str

        """
        self.swagger_types = {
            'body_key': 'str',
            'url_key': 'str',
            'title_key': 'str',
            'embedding_body_key': 'str'
        }

        self.attribute_map = {
            'body_key': 'bodyKey',
            'url_key': 'urlKey',
            'title_key': 'titleKey',
            'embedding_body_key': 'embeddingBodyKey'
        }

        self._body_key = None
        self._url_key = None
        self._title_key = None
        self._embedding_body_key = None

    @property
    def body_key(self):
        """
        **[Required]** Gets the body_key of this IndexSchema.
        Body key name.


        :return: The body_key of this IndexSchema.
        :rtype: str
        """
        return self._body_key

    @body_key.setter
    def body_key(self, body_key):
        """
        Sets the body_key of this IndexSchema.
        Body key name.


        :param body_key: The body_key of this IndexSchema.
        :type: str
        """
        self._body_key = body_key

    @property
    def url_key(self):
        """
        Gets the url_key of this IndexSchema.
        URL key that stores the URL of a document, if available.


        :return: The url_key of this IndexSchema.
        :rtype: str
        """
        return self._url_key

    @url_key.setter
    def url_key(self, url_key):
        """
        Sets the url_key of this IndexSchema.
        URL key that stores the URL of a document, if available.


        :param url_key: The url_key of this IndexSchema.
        :type: str
        """
        self._url_key = url_key

    @property
    def title_key(self):
        """
        Gets the title_key of this IndexSchema.
        Title key that stores the Title of a document, if available.


        :return: The title_key of this IndexSchema.
        :rtype: str
        """
        return self._title_key

    @title_key.setter
    def title_key(self, title_key):
        """
        Sets the title_key of this IndexSchema.
        Title key that stores the Title of a document, if available.


        :param title_key: The title_key of this IndexSchema.
        :type: str
        """
        self._title_key = title_key

    @property
    def embedding_body_key(self):
        """
        Gets the embedding_body_key of this IndexSchema.
        Field within customer managed OCI OpenSearch document containing the vector embedding for queries.


        :return: The embedding_body_key of this IndexSchema.
        :rtype: str
        """
        return self._embedding_body_key

    @embedding_body_key.setter
    def embedding_body_key(self, embedding_body_key):
        """
        Sets the embedding_body_key of this IndexSchema.
        Field within customer managed OCI OpenSearch document containing the vector embedding for queries.


        :param embedding_body_key: The embedding_body_key of this IndexSchema.
        :type: str
        """
        self._embedding_body_key = embedding_body_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other