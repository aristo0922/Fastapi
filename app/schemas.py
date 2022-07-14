# 타입 힌트를 지원하기 위한 typing 모듈
# typing ?  https://www.daleseo.com/python-typing/
from typing import Sequence

from pydantic import BaseModel, HttpUrl

# Recipe : BaseModel - from pydantic- 상속
class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl  # 3pydantic HttpUrl 헬퍼 사용
    #  -=> URL 컴포넌트를 어느정도 예측할 수 있도록

# 3  uses Pydantic’s recursive capability to define a field
#   that refers to another Pydantic class we’ve previously defined, the Recipe class
class RecipeSearchResults(BaseModel):
    # 4 Sequence (which is an iterable with support for len and __getitem__) of Recipes.
    results: Sequence[Recipe]

# ????????? >https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-4-pydantic-schemas/