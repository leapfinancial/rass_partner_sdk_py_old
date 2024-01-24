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



from pydantic import BaseModel, Field, StrictBool

class IsPhoneAvailableResponse(BaseModel):
    """
    IsPhoneAvailableResponse
    """
    available: StrictBool = Field(..., description="If the phone is already in use, this field will be set to false.")
    verified: StrictBool = Field(..., description="If the phone is verified by SMS, this field will be set to true.")
    has_pincode: StrictBool = Field(..., alias="hasPincode", description="If the user already set a pincode for this phone, this field will be set to true.")
    __properties = ["available", "verified", "hasPincode"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IsPhoneAvailableResponse:
        """Create an instance of IsPhoneAvailableResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IsPhoneAvailableResponse:
        """Create an instance of IsPhoneAvailableResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IsPhoneAvailableResponse.parse_obj(obj)

        _obj = IsPhoneAvailableResponse.parse_obj({
            "available": obj.get("available"),
            "verified": obj.get("verified"),
            "has_pincode": obj.get("hasPincode")
        })
        return _obj


