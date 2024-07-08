import enum
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class StatusEnum(str, enum.Enum):
    active = "active"
    suspended = "suspended"
    provision = "provision"


class CableModem(BaseModel):
    """Cable Modem model."""

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: uuid.UUID
    model: str
    description: str
    status: StatusEnum
    valid_since: datetime
    tags: list[str]


class CableModemPayload(BaseModel):
    """Cable Modem payload model."""

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    model: str = Field(..., min_length=1, max_length=256)
    description: str = Field(..., min_length=1, max_length=256)
    status: StatusEnum
    valid_since: datetime
    tags: list[str]


class SortByEnum(str, enum.Enum):
    name = "name"
    status = "status"


class FilterParams(BaseModel):
    name: str | None = None
    status: StatusEnum | None = None
    sort_by: SortByEnum | None = None
