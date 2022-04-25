"""
Так как размер проекта сейчас небольшой, то все части проекта лежат в одной директории в отдельных файлах.

При разрастании кодовой базы следует разложить модули по отдельным папкам, например, repositories/, tests/, ...

В тестах полезно писать побольше текста. IMHO.
"""

import pytest
import sqlite3
import os

from repositories import NameRepository

TEST_DATABASE = os.getenv("DATABASE_FILE")

def test_name_repository():
    """
    проверим работоспособность репозитория данных с именами и фамилиями
    """
    repo = NameRepository(TEST_DATABASE)
    # просто проверим что бд работает и отдаёт ожидаемое кол-во данных
    assert len(repo.get_names(count=10)) == 10
    assert len(repo.get_second_names(count=10)) == 10


    





