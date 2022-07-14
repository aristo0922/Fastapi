from fastapi import FastAPI, APIRouter

from typing import Optional
from app.schemas import RecipeSearchResults, Recipe

# pydantic: 데이터 검증과 파이썬 타입 어노테이션을 통한 management settings
from pydantic import BaseModel, HttpUrl

class Car(BaseModel):
    brand: str
    color: str
    gears: int


class ParkingLot(BaseModel):
    cars: list[Car]  # recursively use `Car`
    spaces: int

# 1 딕셔너리 형태로 예시 데이터 생성
RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]

# 1
app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

# 2 APIRouter 인스턴스화
api_router = APIRouter()

# 3 어노테이션? 데코레이터! get메소드 정의.
# Define a basic GET endpoint for API
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}

# 매개변수 타입 str로 수정 -> str을 통해 매개변수를 받음 : 파라미터 타입 검증
# 타입 힌트를 통한 input mistakes 방지
# 1 Updated to use a 'response_model'
# Recipe > BaseModel > BaseModel : 상속
@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]



# New addition, query parameter
# https://fastapi.tiangolo.com/tutorial/query-params/
@api_router.get("/search/", status_code=200)
def search_recipes(
        #  ex > http://localhost:8001/search/?keyword=chicken&max_results=2
        # arguments >>   keyword      || max results : default value = 10 (Option)
        keyword: Optional[str] = None, max_results: Optional[int] = 10
        #Optional : from Python standard library typing module
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}

    # search -> serialized to JSON by the framework
    # lambda 매개변수:표현식 ? f(recipe)=keyword.label.lower() https://wikidocs.net/64
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


# 4
app.include_router(api_router)

# 5 모듈이 불릴 때 적용
# main.py 를 실행할 때 불림
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
