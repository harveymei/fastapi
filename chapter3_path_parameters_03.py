from enum import Enum
from fastapi import FastAPI

# 定义一个枚举类 UserType，用于表示用户类型
# 继承自 str 和 Enum，使得枚举值可以作为字符串使用，并且支持 FastAPI 的路径参数解析
class UserType(str, Enum):
    STANDARD = "standard"  # 标准用户
    ADMIN = "admin"        # 管理员用户

# 创建 FastAPI 应用实例
app = FastAPI()

# 定义一个 GET 请求路由，路径为 "/users/{types}/{idn}"
# {types} 是路径参数，类型为 UserType 枚举
# {idn} 是路径参数，类型为 int，表示用户的唯一标识符
@app.get("/users/{types}/{idn}")
async def get_user(types: UserType, idn: int):
    """
    获取指定类型的用户信息。

    参数:
    - types (UserType): 用户类型，必须是 'standard' 或 'admin'
    - idn (int): 用户的唯一标识符，必须是整数

    返回:
    - dict: 包含用户类型和 ID 的字典
    """
    return {"type": types, "id": idn}
