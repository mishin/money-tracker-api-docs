# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ExpenseResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, amount=None, date=None, content=None):  # noqa: E501
        """ExpenseResponse - a model defined in OpenAPI

        :param id: The id of this ExpenseResponse.  # noqa: E501
        :type id: str
        :param amount: The amount of this ExpenseResponse.  # noqa: E501
        :type amount: int
        :param date: The date of this ExpenseResponse.  # noqa: E501
        :type date: date
        :param content: The content of this ExpenseResponse.  # noqa: E501
        :type content: str
        """
        self.openapi_types = {
            'id': str,
            'amount': int,
            'date': date,
            'content': str
        }

        self.attribute_map = {
            'id': 'id',
            'amount': 'amount',
            'date': 'date',
            'content': 'content'
        }

        self._id = id
        self._amount = amount
        self._date = date
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'ExpenseResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExpenseResponse of this ExpenseResponse.  # noqa: E501
        :rtype: ExpenseResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ExpenseResponse.

        支出ID  # noqa: E501

        :return: The id of this ExpenseResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpenseResponse.

        支出ID  # noqa: E501

        :param id: The id of this ExpenseResponse.
        :type id: str
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this ExpenseResponse.

        支出額  # noqa: E501

        :return: The amount of this ExpenseResponse.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ExpenseResponse.

        支出額  # noqa: E501

        :param amount: The amount of this ExpenseResponse.
        :type amount: int
        """
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this ExpenseResponse.

        支出日付  # noqa: E501

        :return: The date of this ExpenseResponse.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ExpenseResponse.

        支出日付  # noqa: E501

        :param date: The date of this ExpenseResponse.
        :type date: date
        """

        self._date = date

    @property
    def content(self):
        """Gets the content of this ExpenseResponse.

        支出内容  # noqa: E501

        :return: The content of this ExpenseResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ExpenseResponse.

        支出内容  # noqa: E501

        :param content: The content of this ExpenseResponse.
        :type content: str
        """

        self._content = content
