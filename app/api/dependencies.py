from collections.abc import Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models, repository, session


def get_repository(
    model: type[models.Base],
) -> Callable[[AsyncSession], repository.DatabaseRepository]:
    """
    Returns a dependency function that provides a database repository for a given model.

    Args:
        model (type[models.Base]): The model class for which the repository is created.

    Returns:
        Callable[[AsyncSession], repository.DatabaseRepository]: The dependency function that provides the database repository.

    Example usage:
        repository_dependency = get_repository(CableModem)
        cm_repository = repository_dependency(db_session)
    """
    def func(session: AsyncSession = Depends(session.get_db_session)):
        return repository.DatabaseRepository(model, session)

    return func
