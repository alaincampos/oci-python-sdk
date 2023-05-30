# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbSchemaObjectSummary(object):
    """
    Details for a given object id
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbSchemaObjectSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AddmDbSchemaObjectSummary.
        :type id: str

        :param object_identifier:
            The value to assign to the object_identifier property of this AddmDbSchemaObjectSummary.
        :type object_identifier: int

        :param owner:
            The value to assign to the owner property of this AddmDbSchemaObjectSummary.
        :type owner: str

        :param object_name:
            The value to assign to the object_name property of this AddmDbSchemaObjectSummary.
        :type object_name: str

        :param sub_object_name:
            The value to assign to the sub_object_name property of this AddmDbSchemaObjectSummary.
        :type sub_object_name: str

        :param object_type:
            The value to assign to the object_type property of this AddmDbSchemaObjectSummary.
        :type object_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'object_identifier': 'int',
            'owner': 'str',
            'object_name': 'str',
            'sub_object_name': 'str',
            'object_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'object_identifier': 'objectIdentifier',
            'owner': 'owner',
            'object_name': 'objectName',
            'sub_object_name': 'subObjectName',
            'object_type': 'objectType'
        }

        self._id = None
        self._object_identifier = None
        self._owner = None
        self._object_name = None
        self._sub_object_name = None
        self._object_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AddmDbSchemaObjectSummary.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AddmDbSchemaObjectSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddmDbSchemaObjectSummary.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AddmDbSchemaObjectSummary.
        :type: str
        """
        self._id = id

    @property
    def object_identifier(self):
        """
        **[Required]** Gets the object_identifier of this AddmDbSchemaObjectSummary.
        Object id (from RDBMS)


        :return: The object_identifier of this AddmDbSchemaObjectSummary.
        :rtype: int
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier):
        """
        Sets the object_identifier of this AddmDbSchemaObjectSummary.
        Object id (from RDBMS)


        :param object_identifier: The object_identifier of this AddmDbSchemaObjectSummary.
        :type: int
        """
        self._object_identifier = object_identifier

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this AddmDbSchemaObjectSummary.
        Owner of object


        :return: The owner of this AddmDbSchemaObjectSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this AddmDbSchemaObjectSummary.
        Owner of object


        :param owner: The owner of this AddmDbSchemaObjectSummary.
        :type: str
        """
        self._owner = owner

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this AddmDbSchemaObjectSummary.
        Name of object


        :return: The object_name of this AddmDbSchemaObjectSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this AddmDbSchemaObjectSummary.
        Name of object


        :param object_name: The object_name of this AddmDbSchemaObjectSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def sub_object_name(self):
        """
        Gets the sub_object_name of this AddmDbSchemaObjectSummary.
        Subobject name; for example, partition name


        :return: The sub_object_name of this AddmDbSchemaObjectSummary.
        :rtype: str
        """
        return self._sub_object_name

    @sub_object_name.setter
    def sub_object_name(self, sub_object_name):
        """
        Sets the sub_object_name of this AddmDbSchemaObjectSummary.
        Subobject name; for example, partition name


        :param sub_object_name: The sub_object_name of this AddmDbSchemaObjectSummary.
        :type: str
        """
        self._sub_object_name = sub_object_name

    @property
    def object_type(self):
        """
        **[Required]** Gets the object_type of this AddmDbSchemaObjectSummary.
        Type of the object (such as TABLE, INDEX)


        :return: The object_type of this AddmDbSchemaObjectSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AddmDbSchemaObjectSummary.
        Type of the object (such as TABLE, INDEX)


        :param object_type: The object_type of this AddmDbSchemaObjectSummary.
        :type: str
        """
        self._object_type = object_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other