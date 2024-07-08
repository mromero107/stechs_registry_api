import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api import models
from app.api.dependencies import get_repository
from app.database import models as db_models
from app.database.repository import DatabaseRepository

router = APIRouter(tags=["CableModems"])

CableModemRepository = Annotated[
    DatabaseRepository[db_models.CableModem],
    Depends(get_repository(db_models.CableModem)),
]


@router.post("/cableModems", status_code=status.HTTP_201_CREATED)
async def create_cable_modem(
    data: models.CableModemPayload,
    repository: CableModemRepository,
) -> models.CableModem:
    """
    Create a new cable modem.

    Args:
        data (models.CableModemPayload): The payload containing the data for the new cable modem.
        repository (CableModemRepository): The repository for accessing the database.

    Returns:
        models.CableModem: The created cable modem.
    """
    cm = await repository.create(data.model_dump())
    return models.CableModem.model_validate(cm)


@router.get("/cableModems", status_code=status.HTTP_200_OK)
async def get_cable_modems(
    repository: CableModemRepository,
    params: models.FilterParams = Depends(models.FilterParams),
) -> list[models.CableModem]:
    """
    Get a list of cable modems.

    Args:
        repository (CableModemRepository): The repository for accessing the database.
        params (models.FilterParams, optional): The filter parameters for the cable modems. Defaults to None.

    Returns:
        list[models.CableModem]: The list of cable modems.
    """
    expressions = []
    sort_expression = None
    if params.name:
        expressions.append(db_models.CableModem.model.icontains(params.name))
    if params.status:
        expressions.append(db_models.CableModem.status == params.status.value)

    if params.sort_by == "name":
        sort_expression = db_models.CableModem.model
    elif params.sort_by == "status":
        sort_expression = db_models.CableModem.status

    cms = await repository.filter(*expressions, sort_expression=sort_expression)

    return [models.CableModem.model_validate(cm) for cm in cms]


@router.get("/cableModems/{id}", status_code=status.HTTP_200_OK)
async def get_cable_modem(
    id: uuid.UUID,
    repository: CableModemRepository,
) -> models.CableModem:
    """
    Get a specific cable modem by ID.

    Args:
        id (uuid.UUID): The ID of the cable modem.
        repository (CableModemRepository): The repository for accessing the database.

    Returns:
        models.CableModem: The cable modem with the specified ID.

    Raises:
        HTTPException: If the cable modem does not exist.
    """
    cm = await repository.get(id)
    if cm is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CableModem does not exist",
        )
    return models.CableModem.model_validate(cm)
