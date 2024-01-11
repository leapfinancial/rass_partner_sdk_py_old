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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from raassdkpy.models.raa_s_payment_method import RaaSPaymentMethod
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SendMoneyBase(BaseModel):
    """
    SendMoneyBase
    """ # noqa: E501
    correlation_id: StrictStr = Field(alias="correlationId")
    source_payment_method: RaaSPaymentMethod = Field(alias="sourcePaymentMethod")
    destination_payment_method: Optional[RaaSPaymentMethod] = Field(default=None, alias="destinationPaymentMethod")
    amount: Union[StrictFloat, StrictInt]
    currency: StrictStr
    code: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    sender_amount: Union[StrictFloat, StrictInt] = Field(alias="senderAmount")
    sender_currency: StrictStr = Field(alias="senderCurrency")
    recipient_amount: Union[StrictFloat, StrictInt] = Field(alias="recipientAmount")
    recipient_currency: StrictStr = Field(alias="recipientCurrency")
    fee_type: StrictStr = Field(alias="feeType")
    source_fee: Union[StrictFloat, StrictInt] = Field(alias="sourceFee")
    transaction_fee: Union[StrictFloat, StrictInt] = Field(alias="transactionFee")
    destination_fee: Union[StrictFloat, StrictInt] = Field(alias="destinationFee")
    exchange_rate: Union[StrictFloat, StrictInt] = Field(alias="exchangeRate")
    call_location_longitude: Union[StrictFloat, StrictInt] = Field(alias="callLocationLongitude")
    call_location_latitude: Union[StrictFloat, StrictInt] = Field(alias="callLocationLatitude")
    reason: Optional[StrictStr] = None
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    user_tenant_id: Optional[StrictStr] = Field(default=None, alias="userTenantId")
    tenant_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tenantFee")
    __properties: ClassVar[List[str]] = ["correlationId", "sourcePaymentMethod", "destinationPaymentMethod", "amount", "currency", "code", "status", "senderAmount", "senderCurrency", "recipientAmount", "recipientCurrency", "feeType", "sourceFee", "transactionFee", "destinationFee", "exchangeRate", "callLocationLongitude", "callLocationLatitude", "reason", "tenantId", "userTenantId", "tenantFee"]

    @field_validator('fee_type')
    def fee_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('UserPays', 'ThirdPartyPays', 'SplitPay'):
            raise ValueError("must be one of enum values ('UserPays', 'ThirdPartyPays', 'SplitPay')")
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
        """Create an instance of SendMoneyBase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_payment_method
        if self.source_payment_method:
            _dict['sourcePaymentMethod'] = self.source_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_payment_method
        if self.destination_payment_method:
            _dict['destinationPaymentMethod'] = self.destination_payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SendMoneyBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "correlationId": obj.get("correlationId"),
            "sourcePaymentMethod": RaaSPaymentMethod.from_dict(obj.get("sourcePaymentMethod")) if obj.get("sourcePaymentMethod") is not None else None,
            "destinationPaymentMethod": RaaSPaymentMethod.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "code": obj.get("code"),
            "status": obj.get("status"),
            "senderAmount": obj.get("senderAmount"),
            "senderCurrency": obj.get("senderCurrency"),
            "recipientAmount": obj.get("recipientAmount"),
            "recipientCurrency": obj.get("recipientCurrency"),
            "feeType": obj.get("feeType"),
            "sourceFee": obj.get("sourceFee"),
            "transactionFee": obj.get("transactionFee"),
            "destinationFee": obj.get("destinationFee"),
            "exchangeRate": obj.get("exchangeRate"),
            "callLocationLongitude": obj.get("callLocationLongitude"),
            "callLocationLatitude": obj.get("callLocationLatitude"),
            "reason": obj.get("reason"),
            "tenantId": obj.get("tenantId"),
            "userTenantId": obj.get("userTenantId"),
            "tenantFee": obj.get("tenantFee")
        })
        return _obj

