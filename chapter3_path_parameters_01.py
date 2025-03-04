from fastapi import FastAPI

# 创建一个 FastAPI 应用实例
app = FastAPI()

# 定义一个 GET 请求的路由，路径包含路径参数 {idn}
@app.get("/users/{idn}")
# 定义异步处理函数，当访问 /users/{idn} 路径时触发
# 参数 idn 是从 URL 中提取的路径参数，并指定为整数类型 (int)
async def get_user(idn: int):
    # 返回 JSON 响应，内容为 {"id": idn}
    return {"id": idn}

"""
FastAPI：用于创建 FastAPI 应用实例。
@app.get("/users/{idn}")：装饰器，定义了一个 HTTP GET 请求的路由，路径为 /users/{idn}。
其中 {idn} 是路径参数，表示该位置的值将作为参数传递给处理函数。
async def get_user(idn: int)：定义了一个异步函数，作为处理该路由的逻辑。idn 是从 URL 中提取的路径参数，并且被指定为整数类型 (int)。
return {"id": idn}：返回一个 JSON 响应，内容是键值对 "id": idn，其中 idn 是从 URL 中提取的路径参数值。
"""