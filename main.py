from fastapi import FastAPI, APIRouter
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

# 2 - New addition, path parameter
# https://fastapi.tiangolo.com/tutorial/path-params/
# create endpoint /recipe/{recipe_id}
# endpoint ? one end of a communication channel -> 채널 한쪽 끝에 해당하는 URL
# endpoint 설정
@api_router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:  # 3 defines the logic for the new endpoint
    # endpoint 로직 정의
    """
    Fetch a single recipe by ID
    """
    # 리스트, 반복문, 조건문
    # 4 json 형식으로 serialized 되어 반환
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]

# 4
app.include_router(api_router)

# 5 모듈이 불릴 때 적용
# main.py 를 실행할 때 불림
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
