# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HumanEvaluation(pydantic.BaseModel):
    id: str
    app_id: str
    user_id: str
    user_username: str
    evaluation_type: str
    variant_ids: typing.List[str]
    variant_names: typing.List[str]
    variants_revision_ids: typing.List[str]
    revisions: typing.List[str]
    testset_id: str
    testset_name: str
    status: str
    created_at: dt.datetime
    updated_at: dt.datetime

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}