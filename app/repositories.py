import sqlite3
from typing import List, Text, Tuple
import logging

logger = logging.getLogger("repositories")


class NameRepository:
    def __init__(self, database_file: str):
        try:
            self.db = sqlite3.connect(database_file)
        except Exception as e:
            logger.exception(e)

    def get_names(self, count: int = 0, gender: int = 0) -> List[Tuple[Text, int]]:
        """
        get_names return list of tuples each with the name and the gender for the name.

        names can be selected by specific gender (1 for man, 2 for woman), or both (gender = 0).

        count = 0 and gender = 0 when we want all names from database.
        """
        try:
            # формировать запросы к бд таким образом не самый безопасный способ, но
            # мы приводим параметры к типу int.
            # плюс pydantic валидация входных данных.

            if gender != 0:
                GENDER_WHERE = f" WHERE gender = {int(gender)}"
            else:
                GENDER_WHERE = ""

            if count != 0:
                COUNT_LIMIT = f" LIMIT {int(count)}"
            else:
                COUNT_LIMIT = ""
            SELECT_SQL = "SELECT * FROM names" + GENDER_WHERE + COUNT_LIMIT + ";"

            cursor = self.db.cursor()
            cursor.execute(SELECT_SQL)
            results = cursor.fetchall()
            cursor.close()

            return results
            
        except Exception as e:
            logger.exception(e)


    def get_second_names(self, count: int = 0, gender: int = 0) -> List[Tuple[Text, int]]:
        """
        pretty much the same as get_names but for second_names

        copy/paste
        """
        try:
            if gender != 0:
                GENDER_WHERE = f" WHERE gender = {int(gender)}"
            else:
                GENDER_WHERE = ""

            if count != 0:
                COUNT_LIMIT = f" LIMIT {int(count)}"
            else:
                COUNT_LIMIT = ""
            SELECT_SQL = "SELECT * FROM second_names" + GENDER_WHERE + COUNT_LIMIT + ";"

            cursor = self.db.cursor()
            cursor.execute(SELECT_SQL)
            results = cursor.fetchall()
            cursor.close()

            return results
            
        except Exception as e:
            logger.exception(e)
