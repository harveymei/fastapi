from fastapi import FastAPI
# 创建一个 FastAPI 应用实例
app = FastAPI()

# 定义一个 GET 请求的路由，路径为根路径 "/"
@app.get("/")
# 定义异步处理函数，当访问根路径时触发
async def helloworld():
    # 返回 JSON 响应，内容为 {"hello": "world"}
    return {"hello": "world"}

"""
(.venv) harveymei@A2402:~/PycharmProjects/fastapi$ uvicorn chapter3_first_endpoint_01:app
INFO:     Started server process [23668]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
"""