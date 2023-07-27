import random
from typing import Optional, List, Annotated

import uvicorn
from faker import Faker
from faker.providers import BaseProvider

from fastapi import FastAPI, Query

from fields import available_fields

app = FastAPI()


def get_fake_data(fake: Faker, methods: List[str]):
    data = {}
    for provider in fake.get_providers():
        if isinstance(provider, BaseProvider):
            provider_methods = [method for method in dir(provider) if method[0] != "_"]
            for method in methods:
                if method in provider_methods:
                    data[method] = getattr(provider, method)()
    return data


@app.get("/", name="List of available routes")
async def get_index():
    skip_route_names = ["openapi", "swagger_ui_redirect"]

    routes = [
        {"methods": route.methods, "path": route.path, "name": route.name}
        for route in app.routes
        if route.name not in skip_route_names
    ]
    return routes


@app.get("/available_fields", name="List of available fields")
async def get_fields(locale: Optional[str] = 'en_US'):
    fake = Faker(locale)
    return get_fake_data(fake, available_fields)


@app.get("/{any}", name="Dynamic data getter")
async def get_data(
        locale: Optional[str] = 'en_US',
        limit: Annotated[int, Query(gt=1, lt=500)] = 10,
        fields: Optional[str] = None
):
    fake = Faker(locale)
    field_list = [field.strip() for field in fields.split(',')] if fields else []
    if not field_list:
        field_list = random.choices(available_fields, k=6)

    data = []
    for _ in range(limit):
        data.append(get_fake_data(fake, field_list))

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
