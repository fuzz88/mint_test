import os
from fastapi import FastAPI, Query

from controllers import FakeIdentityDataController, FakeIdentityGenerator
from repositories import NameRepository
from constants import Gender

app = FastAPI()

controller = FakeIdentityDataController(
    generator=FakeIdentityGenerator(NameRepository(os.getenv("DATABASE_FILE")))
)


@app.get("/persons")
async def persons(
    start_age: int = Query(18, ge=1, le=99),
    end_age: int = Query(95, ge=1, le=99),
    gender: int = Query(Gender.BOTH, ge=Gender.BOTH, le=Gender.FEMALE),
    count: int = Query(10, ge=1, le=1000),
):

    return controller.generate_fake_identities(count, start_age, end_age, gender)
