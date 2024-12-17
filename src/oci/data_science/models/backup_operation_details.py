# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupOperationDetails(object):
    """
    Backup operation details of the model.
    """

    #: A constant which can be used with the backup_state property of a BackupOperationDetails.
    #: This constant has a value of "PENDING"
    BACKUP_STATE_PENDING = "PENDING"

    #: A constant which can be used with the backup_state property of a BackupOperationDetails.
    #: This constant has a value of "FAILED"
    BACKUP_STATE_FAILED = "FAILED"

    #: A constant which can be used with the backup_state property of a BackupOperationDetails.
    #: This constant has a value of "SUCCEEDED"
    BACKUP_STATE_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new BackupOperationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_last_backup:
            The value to assign to the time_last_backup property of this BackupOperationDetails.
        :type time_last_backup: datetime

        :param backup_state:
            The value to assign to the backup_state property of this BackupOperationDetails.
            Allowed values for this property are: "PENDING", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_state: str

        :param backup_state_details:
            The value to assign to the backup_state_details property of this BackupOperationDetails.
        :type backup_state_details: str

        """
        self.swagger_types = {
            'time_last_backup': 'datetime',
            'backup_state': 'str',
            'backup_state_details': 'str'
        }

        self.attribute_map = {
            'time_last_backup': 'timeLastBackup',
            'backup_state': 'backupState',
            'backup_state_details': 'backupStateDetails'
        }

        self._time_last_backup = None
        self._backup_state = None
        self._backup_state_details = None

    @property
    def time_last_backup(self):
        """
        Gets the time_last_backup of this BackupOperationDetails.
        The last backup execution time of the model.


        :return: The time_last_backup of this BackupOperationDetails.
        :rtype: datetime
        """
        return self._time_last_backup

    @time_last_backup.setter
    def time_last_backup(self, time_last_backup):
        """
        Sets the time_last_backup of this BackupOperationDetails.
        The last backup execution time of the model.


        :param time_last_backup: The time_last_backup of this BackupOperationDetails.
        :type: datetime
        """
        self._time_last_backup = time_last_backup

    @property
    def backup_state(self):
        """
        **[Required]** Gets the backup_state of this BackupOperationDetails.
        The backup status of the model.

        Allowed values for this property are: "PENDING", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_state of this BackupOperationDetails.
        :rtype: str
        """
        return self._backup_state

    @backup_state.setter
    def backup_state(self, backup_state):
        """
        Sets the backup_state of this BackupOperationDetails.
        The backup status of the model.


        :param backup_state: The backup_state of this BackupOperationDetails.
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(backup_state, allowed_values):
            backup_state = 'UNKNOWN_ENUM_VALUE'
        self._backup_state = backup_state

    @property
    def backup_state_details(self):
        """
        **[Required]** Gets the backup_state_details of this BackupOperationDetails.
        The backup execution status details of the model.


        :return: The backup_state_details of this BackupOperationDetails.
        :rtype: str
        """
        return self._backup_state_details

    @backup_state_details.setter
    def backup_state_details(self, backup_state_details):
        """
        Sets the backup_state_details of this BackupOperationDetails.
        The backup execution status details of the model.


        :param backup_state_details: The backup_state_details of this BackupOperationDetails.
        :type: str
        """
        self._backup_state_details = backup_state_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other