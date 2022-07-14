from fastapi import FastAPI, APIRouter

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

# 4
app.include_router(api_router)


# 5 모듈이 불릴 때 적용
# main.py 를 실행할 때 불림
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")