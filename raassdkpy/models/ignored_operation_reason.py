# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IgnoredOperationReason(str, Enum):
    """
    IgnoredOperationReason
    """

    """
    allowed enum values
    """
    I_DONT_RECOGNIZE_CONTACT = 'I_DONT_RECOGNIZE_CONTACT'
    AMOUNT_TOO_HIGHT = 'AMOUNT_TOO_HIGHT'
    I_DONT_HAVE_MONEY_RIGHT_NOW = 'I_DONT_HAVE_MONEY_RIGHT_NOW'
    OTHER = 'OTHER'
    I_DIDNT_MAKE_THIS_REQUEST = 'I_DIDNT_MAKE_THIS_REQUEST'
    I_REQUESTED_A_DIFFERENT_AMOUNT = 'I_REQUESTED_A_DIFFERENT_AMOUNT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IgnoredOperationReason from a JSON string"""
        return cls(json.loads(json_str))

