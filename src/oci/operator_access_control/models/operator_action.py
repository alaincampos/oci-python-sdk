# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatorAction(object):
    """
    Details of the operator action. Operator actions are a pre-defined set of commands available to the operator on different layers of the infrastructure. Although the groupings may differ depending on the infrastructure layers,
    the groups are designed to enable the operator access to commands to resolve a specific set of issues. The infrastructure layers controlled by the Operator Control include Dom0, CellServer, and Control Plane Server (CPS).

    There are five groups available to the operator. x-obmcs-top-level-enum: '#/definitions/OperatorActionCategories' enum: *OPERATORACTIONCATEGORIES

    The following infrastructure layers are controlled by the operator actions x-obmcs-top-level-enum: '#/definitions/InfrastructureLayers' enum: *INFRASTRUCTURELAYERS
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OperatorAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperatorAction.
        :type id: str

        :param name:
            The value to assign to the name property of this OperatorAction.
        :type name: str

        :param component:
            The value to assign to the component property of this OperatorAction.
        :type component: str

        :param description:
            The value to assign to the description property of this OperatorAction.
        :type description: str

        :param properties:
            The value to assign to the properties property of this OperatorAction.
        :type properties: list[oci.operator_access_control.models.OperatorActionProperties]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'component': 'str',
            'description': 'str',
            'properties': 'list[OperatorActionProperties]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'component': 'component',
            'description': 'description',
            'properties': 'properties'
        }

        self._id = None
        self._name = None
        self._component = None
        self._description = None
        self._properties = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperatorAction.
        Unique Oracle assigned identifier for the operator action.


        :return: The id of this OperatorAction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperatorAction.
        Unique Oracle assigned identifier for the operator action.


        :param id: The id of this OperatorAction.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OperatorAction.
        Name of the operator action.


        :return: The name of this OperatorAction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OperatorAction.
        Name of the operator action.


        :param name: The name of this OperatorAction.
        :type: str
        """
        self._name = name

    @property
    def component(self):
        """
        Gets the component of this OperatorAction.
        Name of the infrastructure layer associated with the operator action.


        :return: The component of this OperatorAction.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this OperatorAction.
        Name of the infrastructure layer associated with the operator action.


        :param component: The component of this OperatorAction.
        :type: str
        """
        self._component = component

    @property
    def description(self):
        """
        Gets the description of this OperatorAction.
        Description of the operator action in terms of associated risk profile, and characteristics of the operating system commands made
        available to the operator under this operator action.


        :return: The description of this OperatorAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OperatorAction.
        Description of the operator action in terms of associated risk profile, and characteristics of the operating system commands made
        available to the operator under this operator action.


        :param description: The description of this OperatorAction.
        :type: str
        """
        self._description = description

    @property
    def properties(self):
        """
        Gets the properties of this OperatorAction.
        Fine grained properties associated with the operator control.


        :return: The properties of this OperatorAction.
        :rtype: list[oci.operator_access_control.models.OperatorActionProperties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this OperatorAction.
        Fine grained properties associated with the operator control.


        :param properties: The properties of this OperatorAction.
        :type: list[oci.operator_access_control.models.OperatorActionProperties]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
