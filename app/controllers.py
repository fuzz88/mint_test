import datetime
import random
import uuid
from typing import Generator, List, Text, Tuple

from dtos import FakeIdentity
from repositories import NameRepository

"""
TODO: развязать все объекты через интерфейсы (абстрактные классы), т.е. реализовать правильную иерархию классов.
"""


class FakeIdentityGenerator:
    """
    Generates fake identities based on NameRepository as data source.
    """

    def __init__(self, repo: NameRepository):
        self.repo = repo
        # получаем сразу все данные для имени и фамилии
        self.names = self.repo.get_names()
        self.second_names = self.repo.get_second_names()

    def pick_random_names(self, gender: int) -> Tuple[Text, Text]:
        """
        Picks the name and the second_name of the same gender.
        """
        names_count = len(self.names)
        second_names_count = len(self.second_names)

        # TODO: DRY?
        name = None
        while name is None:
            picked_index = random.randint(0, names_count - 1)
            if self.names[picked_index][1] == gender:
                name = self.names[picked_index][0]

        second_name = None
        while second_name is None:
            picked_index = random.randint(0, second_names_count - 1)
            if self.second_names[picked_index][1] == gender:
                second_name = self.second_names[picked_index][0]

        return name, second_name

    def pick_date_of_birth(self, start_age: int, end_age: int) -> str:
        """
        Picks random birth date for the age's range given.
        Fuzzy: counts only years. Some dates are skipped, because of february, etc.
        """
        if end_age < start_age:
            raise ValueError("wrong age")
        year_now = datetime.date.today().year
        # чем больше возраст, тем раньше год
        year_of_birth_end = year_now - start_age
        year_of_birth_start = year_now - end_age
        date_of_birth = datetime.date(
            random.randint(year_of_birth_start, year_of_birth_end),
            month=random.randint(1, 12),
            day=random.randint(1, 25),
        )
        return date_of_birth.strftime("%d.%m.%Y")

    def get_identity_generator(
        self, gender: int, start_age: int, end_age: int
    ) -> Generator:
        def iter_identities() -> FakeIdentity:
            while True:
                name, second_name = self.pick_random_names(gender=gender)
                date_of_birth = self.pick_date_of_birth(
                    start_age=start_age, end_age=end_age
                )
                gndr = "муж." if gender == 1 else "жен."
                # TODO: obviously fake) refactor
                login = str(uuid.uuid4())
                password = str(uuid.uuid4())
                yield FakeIdentity(
                    name=name,
                    second_name=second_name,
                    gender=gndr,
                    date_of_birth=date_of_birth,
                    login=login,
                    password=password,
                )

        return iter_identities()


class FakeIdentityDataController:
    """
    Uses FakeIdentityGenerator instance to generate data for API.
    """

    def __init__(self, generator: FakeIdentityGenerator):
        self.generator = generator

    def generate_fake_identities(
        self, count: int, start_age: int, end_age: int, gender_pick: int
    ) -> List[FakeIdentity]:
        results = []
        match gender_pick:
            case 1:
                male_generator = self.generator.get_identity_generator(
                    gender=1, start_age=start_age, end_age=end_age
                )
                generated = 0
                while generated < count:
                    results.append(next(male_generator))
                    generated += 1
            case 2:
                generated = 0
                female_generator = self.generator.get_identity_generator(
                    gender=2, start_age=start_age, end_age=end_age
                )
                while generated < count:
                    results.append(next(female_generator))
                    generated += 1
            case 0:
                generated = 0
                male_generator = self.generator.get_identity_generator(
                    gender=1, start_age=start_age, end_age=end_age
                )
                female_generator = self.generator.get_identity_generator(
                    gender=2, start_age=start_age, end_age=end_age
                )
                while generated < count:
                    # если нужны личности обоих полов, то генерируем 50 на 50.
                    person = next(male_generator) if random.random() > 0.5 else next(female_generator)
                    results.append(person)
                    generated += 1
        
        return results
