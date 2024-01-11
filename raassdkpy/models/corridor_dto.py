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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from raassdkpy.models.available_payment_methods import AvailablePaymentMethods
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CorridorDTO(BaseModel):
    """
    CorridorDTO
    """ # noqa: E501
    id: StrictStr = Field(alias="Id")
    source_payment_method_type: AvailablePaymentMethods = Field(alias="SourcePaymentMethodType")
    destination_payment_method_type: AvailablePaymentMethods = Field(alias="DestinationPaymentMethodType")
    lower_limit: Union[StrictFloat, StrictInt] = Field(alias="LowerLimit")
    upper_limit: Union[StrictFloat, StrictInt] = Field(alias="UpperLimit")
    fees: Optional[Any] = Field(alias="Fees")
    corridor_requirements: Optional[Any] = Field(alias="CorridorRequirements")
    is_active: StrictBool = Field(alias="IsActive")
    source_country: StrictStr = Field(alias="SourceCountry")
    destination_country: StrictStr = Field(alias="DestinationCountry")
    __properties: ClassVar[List[str]] = ["Id", "SourcePaymentMethodType", "DestinationPaymentMethodType", "LowerLimit", "UpperLimit", "Fees", "CorridorRequirements", "IsActive", "SourceCountry", "DestinationCountry"]

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
        """Create an instance of CorridorDTO from a JSON string"""
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
        # set to None if fees (nullable) is None
        # and model_fields_set contains the field
        if self.fees is None and "fees" in self.model_fields_set:
            _dict['Fees'] = None

        # set to None if corridor_requirements (nullable) is None
        # and model_fields_set contains the field
        if self.corridor_requirements is None and "corridor_requirements" in self.model_fields_set:
            _dict['CorridorRequirements'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CorridorDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "SourcePaymentMethodType": obj.get("SourcePaymentMethodType"),
            "DestinationPaymentMethodType": obj.get("DestinationPaymentMethodType"),
            "LowerLimit": obj.get("LowerLimit"),
            "UpperLimit": obj.get("UpperLimit"),
            "Fees": obj.get("Fees"),
            "CorridorRequirements": obj.get("CorridorRequirements"),
            "IsActive": obj.get("IsActive"),
            "SourceCountry": obj.get("SourceCountry"),
            "DestinationCountry": obj.get("DestinationCountry")
        })
        return _obj

