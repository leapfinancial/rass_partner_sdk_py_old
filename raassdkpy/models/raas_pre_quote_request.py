# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RaasPreQuoteRequest(BaseModel):
    """
    RaasPreQuoteRequest
    """ # noqa: E501
    recipient_id: Optional[StrictStr] = Field(default=None, alias="RecipientId")
    subscriber_id: Optional[StrictStr] = Field(default=None, alias="SubscriberId")
    destination_payment_method: Optional[Any] = Field(alias="DestinationPaymentMethod")
    sender_country_code: StrictStr = Field(alias="SenderCountryCode")
    is_sender_amount: StrictBool = Field(alias="IsSenderAmount")
    amount: Union[StrictFloat, StrictInt] = Field(alias="Amount")
    operation_type: StrictStr = Field(alias="OperationType")
    product_type: StrictStr = Field(alias="ProductType")
    tennant_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="TennantFee")
    __properties: ClassVar[List[str]] = ["RecipientId", "SubscriberId", "DestinationPaymentMethod", "SenderCountryCode", "IsSenderAmount", "Amount", "OperationType", "ProductType", "TennantFee"]

    @field_validator('operation_type')
    def operation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SendFunds', 'RequestFunds', 'WalletLoad', 'WalletTransferOut', 'TopUp', 'RequestTopUp', 'SendFundsVirtualAgent', 'RequestFundsVirtualAgent', 'StorePayment'):
            raise ValueError("must be one of enum values ('SendFunds', 'RequestFunds', 'WalletLoad', 'WalletTransferOut', 'TopUp', 'RequestTopUp', 'SendFundsVirtualAgent', 'RequestFundsVirtualAgent', 'StorePayment')")
        return value

    @field_validator('product_type')
    def product_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Fund', 'Airtime', 'Loan', 'BillPay', 'NotApplicable', 'VirtualAgent', 'Wallet', 'StorePayment', 'NumiService'):
            raise ValueError("must be one of enum values ('Fund', 'Airtime', 'Loan', 'BillPay', 'NotApplicable', 'VirtualAgent', 'Wallet', 'StorePayment', 'NumiService')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RaasPreQuoteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if destination_payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.destination_payment_method is None and "destination_payment_method" in self.model_fields_set:
            _dict['DestinationPaymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RaasPreQuoteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RecipientId": obj.get("RecipientId"),
            "SubscriberId": obj.get("SubscriberId"),
            "DestinationPaymentMethod": obj.get("DestinationPaymentMethod"),
            "SenderCountryCode": obj.get("SenderCountryCode"),
            "IsSenderAmount": obj.get("IsSenderAmount"),
            "Amount": obj.get("Amount"),
            "OperationType": obj.get("OperationType"),
            "ProductType": obj.get("ProductType"),
            "TennantFee": obj.get("TennantFee")
        })
        return _obj

