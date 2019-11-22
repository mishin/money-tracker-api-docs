# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ExpenseRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount=None, date=None, content=None):  # noqa: E501
        """ExpenseRequest - a model defined in OpenAPI

        :param amount: The amount of this ExpenseRequest.  # noqa: E501
        :type amount: int
        :param date: The date of this ExpenseRequest.  # noqa: E501
        :type date: date
        :param content: The content of this ExpenseRequest.  # noqa: E501
        :type content: str
        """
        self.openapi_types = {
            'amount': int,
            'date': date,
            'content': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'date': 'date',
            'content': 'content'
        }

        self._amount = amount
        self._date = date
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'ExpenseRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExpenseRequest of this ExpenseRequest.  # noqa: E501
        :rtype: ExpenseRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this ExpenseRequest.

        支出額  # noqa: E501

        :return: The amount of this ExpenseRequest.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ExpenseRequest.

        支出額  # noqa: E501

        :param amount: The amount of this ExpenseRequest.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this ExpenseRequest.

        支出日付  # noqa: E501

        :return: The date of this ExpenseRequest.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ExpenseRequest.

        支出日付  # noqa: E501

        :param date: The date of this ExpenseRequest.
        :type date: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def content(self):
        """Gets the content of this ExpenseRequest.

        支出内容  # noqa: E501

        :return: The content of this ExpenseRequest.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ExpenseRequest.

        支出内容  # noqa: E501

        :param content: The content of this ExpenseRequest.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
