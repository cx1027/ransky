from pydantic import BaseModel


class ScoreSchema(BaseModel):
    candidate: dict
    job: dict


class ResponseSchema(BaseModel):
    degree: list
    experience: list
    technical_skill: list
    responsibility: list
    certificate: list
    soft_skill: list
