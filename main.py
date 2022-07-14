from fastapi import FastAPI, APIRouter, Query
from typing import Optional
from app.schemas import RecipeSearchResults, Recipe

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

app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}

# Recipe > BaseModel > BaseModel : 상속
@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]



# 1 add a response_model RecipeSerchResults to /search endpoint
@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
        *,
        # 2 Query : add additional validation and requirements to our query params (ex. min_length)
        keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
        max_results: Optional[int] = 10
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}

    # filter -> serialized to JSON by the framework
    # lambda 매개변수:표현식 ? f(recipe)=keyword.label.lower() https://wikidocs.net/64
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}

app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
