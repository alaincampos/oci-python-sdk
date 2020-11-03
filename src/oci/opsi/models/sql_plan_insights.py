# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanInsights(object):
    """
    Represents collection of SQL Plan Insights.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanInsights object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this SqlPlanInsights.
        :type text: str

        :param value:
            The value to assign to the value property of this SqlPlanInsights.
        :type value: int

        :param category:
            The value to assign to the category property of this SqlPlanInsights.
        :type category: str

        """
        self.swagger_types = {
            'text': 'str',
            'value': 'int',
            'category': 'str'
        }

        self.attribute_map = {
            'text': 'text',
            'value': 'value',
            'category': 'category'
        }

        self._text = None
        self._value = None
        self._category = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this SqlPlanInsights.
        SQL Plan Insight text.
        For example `Number of Plans Used`, `Most Executed Plan`,
          `Best Performing Plan`, `Worst Performing Plan`,
          `Plan With Most IO`,
          `Plan with Most CPU`


        :return: The text of this SqlPlanInsights.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this SqlPlanInsights.
        SQL Plan Insight text.
        For example `Number of Plans Used`, `Most Executed Plan`,
          `Best Performing Plan`, `Worst Performing Plan`,
          `Plan With Most IO`,
          `Plan with Most CPU`


        :param text: The text of this SqlPlanInsights.
        :type: str
        """
        self._text = text

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SqlPlanInsights.
        SQL execution plan hash value for a given insight. For example `Most Executed Plan` insight will have value as \"3975467901\"


        :return: The value of this SqlPlanInsights.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SqlPlanInsights.
        SQL execution plan hash value for a given insight. For example `Most Executed Plan` insight will have value as \"3975467901\"


        :param value: The value of this SqlPlanInsights.
        :type: int
        """
        self._value = value

    @property
    def category(self):
        """
        **[Required]** Gets the category of this SqlPlanInsights.
        SQL Insight category. For example PLANS_USED, MOST_EXECUTED, BEST_PERFORMER, WORST_PERFORMER, MOST_CPU or MOST_IO.


        :return: The category of this SqlPlanInsights.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this SqlPlanInsights.
        SQL Insight category. For example PLANS_USED, MOST_EXECUTED, BEST_PERFORMER, WORST_PERFORMER, MOST_CPU or MOST_IO.


        :param category: The category of this SqlPlanInsights.
        :type: str
        """
        self._category = category

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other