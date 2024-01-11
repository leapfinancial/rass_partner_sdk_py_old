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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from pydantic import Field
from raassdkpy.models.errors_cip_process import ErrorsCIPProcess
from raassdkpy.models.level_status import LevelStatus
from raassdkpy.models.level_status_detail import LevelStatusDetail
from raassdkpy.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac_lola_cip import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    cip_level: Union[StrictFloat, StrictInt] = Field(description="this will updated  from event queue", alias="cipLevel")
    has_personal_info: StrictBool = Field(alias="hasPersonalInfo")
    has_proof_of_l_ife: StrictBool = Field(alias="hasProofOfLIfe")
    has_scan_ids: StrictBool = Field(alias="hasScanIds")
    is_perform_level1: StrictBool = Field(alias="isPerformLevel1")
    is_perform_level2: StrictBool = Field(alias="isPerformLevel2")
    profile_and_ocr_similarity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="profileAndOCRSimilarity")
    errors_process: ErrorsCIPProcess = Field(alias="errorsProcess")
    level1status: LevelStatus
    level1status_detail: LevelStatusDetail = Field(alias="level1statusDetail")
    level2status: LevelStatus
    level2status_detail: LevelStatusDetail = Field(alias="level2statusDetail")
    is_document_id_value_validated: Optional[StrictBool] = Field(default=None, description="This will be used when the document id value will be validated. For example The Nufi's CURP validation", alias="isDocumentIdValueValidated")
    is_alternate_flow: Optional[StrictBool] = Field(default=None, description="This is for knowing the specific cip has an alternate flow", alias="isAlternateFlow")
    lola_cip: Optional[PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP] = Field(default=None, alias="lolaCIP")
    __properties: ClassVar[List[str]] = ["cipLevel", "hasPersonalInfo", "hasProofOfLIfe", "hasScanIds", "isPerformLevel1", "isPerformLevel2", "profileAndOCRSimilarity", "errorsProcess", "level1status", "level1statusDetail", "level2status", "level2statusDetail", "isDocumentIdValueValidated", "isAlternateFlow", "lolaCIP"]

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
        """Create an instance of PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of errors_process
        if self.errors_process:
            _dict['errorsProcess'] = self.errors_process.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lola_cip
        if self.lola_cip:
            _dict['lolaCIP'] = self.lola_cip.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cipLevel": obj.get("cipLevel"),
            "hasPersonalInfo": obj.get("hasPersonalInfo"),
            "hasProofOfLIfe": obj.get("hasProofOfLIfe"),
            "hasScanIds": obj.get("hasScanIds"),
            "isPerformLevel1": obj.get("isPerformLevel1"),
            "isPerformLevel2": obj.get("isPerformLevel2"),
            "profileAndOCRSimilarity": obj.get("profileAndOCRSimilarity"),
            "errorsProcess": ErrorsCIPProcess.from_dict(obj.get("errorsProcess")) if obj.get("errorsProcess") is not None else None,
            "level1status": obj.get("level1status"),
            "level1statusDetail": obj.get("level1statusDetail"),
            "level2status": obj.get("level2status"),
            "level2statusDetail": obj.get("level2statusDetail"),
            "isDocumentIdValueValidated": obj.get("isDocumentIdValueValidated"),
            "isAlternateFlow": obj.get("isAlternateFlow"),
            "lolaCIP": PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP.from_dict(obj.get("lolaCIP")) if obj.get("lolaCIP") is not None else None
        })
        return _obj

