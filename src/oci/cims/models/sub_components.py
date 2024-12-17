# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubComponents(object):
    """
    List of subcomponents under a subcategory.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubComponents object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sub_category:
            The value to assign to the sub_category property of this SubComponents.
        :type sub_category: dict(str, str)

        :param schema:
            The value to assign to the schema property of this SubComponents.
        :type schema: str

        """
        self.swagger_types = {
            'sub_category': 'dict(str, str)',
            'schema': 'str'
        }

        self.attribute_map = {
            'sub_category': 'subCategory',
            'schema': 'schema'
        }

        self._sub_category = None
        self._schema = None

    @property
    def sub_category(self):
        """
        Gets the sub_category of this SubComponents.
        Subcategory list.


        :return: The sub_category of this SubComponents.
        :rtype: dict(str, str)
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """
        Sets the sub_category of this SubComponents.
        Subcategory list.


        :param sub_category: The sub_category of this SubComponents.
        :type: dict(str, str)
        """
        self._sub_category = sub_category

    @property
    def schema(self):
        """
        Gets the schema of this SubComponents.
        Schema of a subcategory.


        :return: The schema of this SubComponents.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this SubComponents.
        Schema of a subcategory.


        :param schema: The schema of this SubComponents.
        :type: str
        """
        self._schema = schema

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other