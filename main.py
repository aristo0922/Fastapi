from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Type, Union

from pydantic import BaseModel

app = FastAPI()

# Recipe 클래스는 BaseModel을 상속한다
class Recipe(BaseModel):
    id: int
    label: str
    source: str

raw_recipe = {'id': 1, 'label': 'Lasagna', 'source': 'Grandma Wisdom'}
structured_recipe = Recipe(**raw_recipe)
print(structured_recipe.id)