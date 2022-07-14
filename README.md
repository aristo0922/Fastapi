# Fastapi

fastapi 설치
```
<code>pip install "fastapi[all]"</code>
```

uvicorn 설치
```
pip install "uvicorn[standard]"
```

실행
```
uvicorn main:app --reload
```
---------------------------------------
#ch2
```
# 4 라우팅
app.include_router(api_router)

# 5 모듈이 불릴 때 적용
# main.py 를 실행할 때 불림
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")```
