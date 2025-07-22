from typing import List, Set, Tuple, Dict, Optional, Literal

"""
Optional[T] – значение может быть T или None (аналог T | None в Python 3.10+).

Union[T1, T2, ...] – значение может быть одним из нескольких типов (аналог T1 | T2 в Python 3.10+).

Any – любой тип (отключает проверку типов).

Callable[[T1, T2], R] – функция, принимающая T1, T2 и возвращающая R.

Iterable[T] – объект, поддерживающий итерацию (например, список, генератор).

Sequence[T] – последовательность (список, кортеж, строка).

Mapping[K, V] – отображение (словарь и подобные).

Значение может быть только одним из указанных.

Mode = Literal["read", "write", "execute"]


Асинхронные типы (Awaitable, Coroutine)

async def fetch_data() -> str:
    return "data"

task: Awaitable[str] = fetch_data()

Значение не может быть изменено.

MAX_SIZE: Final[int] = 100
"""

def get_list(items: List[str]) -> List[int]:
    return [
        len(item) for item in items
    ]

def get_tuple_set_dict(items_t: Tuple[int, int, str], items_s: Set[bytes], items_d: Dict[str, str]):
    return items_t, items_s, items_d