import uuid
from typing import Generic, TypeVar

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from app.database import models

Model = TypeVar("Model", bound=models.Base)


class DatabaseRepository(Generic[Model]):
    """Repository for performing database queries.

    This class provides methods for creating, retrieving, and filtering data in the database.

    Args:
        model (type[Model]): The model class associated with the repository.
        session (AsyncSession): The database session to use for executing queries.

    Attributes:
        model (type[Model]): The model class associated with the repository.
        session (AsyncSession): The database session to use for executing queries.
    """

    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, data: dict) -> Model:
        """Create a new instance of the model in the database.

        Args:
            data (dict): The data to populate the new instance with.

        Returns:
            Model: The created instance of the model.
        """
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: uuid.UUID) -> Model | None:
        """Retrieve an instance of the model from the database by its primary key.

        Args:
            pk (uuid.UUID): The primary key of the instance to retrieve.

        Returns:
            Model | None: The retrieved instance of the model, or None if not found.
        """
        return await self.session.get(self.model, pk)

    async def filter(
        self,
        *expressions: list[BinaryExpression] | None,
        sort_expression: Mapped | None,
    ) -> list[Model]:
        """Filter instances of the model in the database based on the provided expressions.

        Args:
            *expressions (list[BinaryExpression] | None): The filter expressions to apply.
            sort_expression (Mapped | None): The sort expression to apply.

        Returns:
            list[Model]: The list of filtered instances of the model.
        """
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)
        if sort_expression:
            query = query.order_by(sort_expression)
        return list(await self.session.scalars(query))
