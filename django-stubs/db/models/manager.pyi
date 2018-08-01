# Stubs for django.db.models.manager (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Permission
from django.db.models.base import Model
from django.db.models.query import QuerySet
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

class BaseManager:
    creation_counter: int = ...
    auto_created: bool = ...
    use_in_migrations: bool = ...
    def __new__(cls: Type[Manager], *args: Any, **kwargs: Any) -> Manager: ...
    model: Any = ...
    name: Any = ...
    _db: Any = ...
    _hints: Any = ...
    def __init__(self) -> None: ...
    def __str__(self): ...
    def deconstruct(
        self
    ) -> Union[
        Tuple[bool, str, None, Tuple[str, str, int, int], Dict[Any, Any]],
        Tuple[bool, str, None, Tuple, Dict[Any, Any]],
    ]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    @classmethod
    def _get_queryset_methods(
        cls, queryset_class: Type[QuerySet]
    ) -> Dict[str, Callable]: ...
    @classmethod
    def from_queryset(cls, queryset_class: Any, class_name: Optional[Any] = ...): ...
    def contribute_to_class(self, model: Type[Model], name: str) -> None: ...
    def _set_creation_counter(self) -> None: ...
    def db_manager(
        self,
        using: Optional[str] = ...,
        hints: Optional[
            Union[Dict[str, Model], Dict[str, LogEntry], Dict[str, Permission]]
        ] = ...,
    ) -> Manager: ...
    @property
    def db(self) -> str: ...
    def get_queryset(self) -> QuerySet: ...
    def all(self) -> QuerySet: ...
    def __eq__(self, other: Optional[Manager]) -> bool: ...
    def __hash__(self): ...

class Manager: ...

class ManagerDescriptor:
    manager: Any = ...
    def __init__(self, manager: Any) -> None: ...
    def __get__(self, instance: Any, cls: Optional[Any] = ...): ...

class EmptyManager(Manager):
    model: Any = ...
    def __init__(self, model: Type[Model]) -> None: ...
    def get_queryset(self): ...