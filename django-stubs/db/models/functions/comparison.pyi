# Stubs for django.db.models.functions.comparison (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models import Func
from typing import Any

from datetime import date, datetime
from decimal import Decimal
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.fields import Field
from django.db.models.sql.compiler import SQLCompiler
from typing import Any, List, Tuple, Union

class Cast(Func):
    function: str = ...
    template: str = ...
    def __init__(
        self, expression: Union[str, date, Decimal], output_field: Field
    ) -> None: ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper, **extra_context: Any
    ) -> Union[Tuple[str, List[datetime]], Tuple[str, List[Any]]]: ...
    def as_mysql(self, compiler: Any, connection: Any): ...
    def as_postgresql(self, compiler: Any, connection: Any): ...

class Coalesce(Func):
    function: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...
    def as_oracle(self, compiler: Any, connection: Any): ...

class Greatest(Func):
    function: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...
    def as_sqlite(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[Any]]: ...

class Least(Func):
    function: str = ...
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...
    def as_sqlite(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Union[Tuple[str, List[datetime]], Tuple[str, List[Any]]]: ...