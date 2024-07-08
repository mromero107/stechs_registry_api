import enum
import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import orm


class StatusEnum(str, enum.Enum):
    active = "active"
    suspended = "suspended"
    provision = "provision"


class Base(orm.DeclarativeBase):
    """Base database model."""

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )


class CableModem(Base):
    """CableModem database model."""

    __tablename__ = "cablemodem"

    model: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    description: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    status: orm.Mapped[StatusEnum] = orm.mapped_column(
        sa.Enum(StatusEnum, name="statusenum"), nullable=False
    )
    valid_since: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime(timezone=True), nullable=False
    )
    tags: orm.Mapped[list[str]] = orm.mapped_column(sa.JSON)
