from pydantic import BaseModel
from humps import camel


def to_camel(string):
    return camel.case(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
