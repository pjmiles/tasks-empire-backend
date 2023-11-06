from fastapi import APIRouter, HTTPException
from config.db import conn
from schemas.index import CreateUser
from models.index import Users as UserModel

user_router = APIRouter(prefix="/api/v1/users")


@user_router.get("/")
async def get_details():
    cursor = conn.cursor()
    cursor.execute("SELECT * from users;")
    users = cursor.fetchall()
    cursor.close()
    return users


@user_router.get("/{id}")
async def get_data(id):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, password from users WHERE id = %s", (id))
    get_user = cursor.fetchone()
    if not get_user:
        raise HTTPException(status_code=404, detail="User not found")
    return get_user


@user_router.post("/")
async def post_data(user: CreateUser):
    cusor = conn.cursor()
    cusor.execute(
        "INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s) RETURNING id, name, email, password",
        (user.id, user.name, user.email, user.password),
    )
    user_data = cusor.fetchone()
    conn.commit()
    return user_data


@user_router.put("/{id}")
async def update_data(id, user_data: CreateUser):
    cusor = conn.cursor()
    cusor.execute(
        "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s RETURNING id, name, email",
        (user_data.name, user_data.email, user_data.password, id),
    )
    update_user = cusor.fetchone()
    conn.commit()
    return update_user


@user_router.delete("/{id}")
async def delete(user_id: int):
    cusor = conn.cursor()
    cusor.execute(
        "DELETE FROM users WHERE id = %s RETURNING id, name, email", (user_id,)
    )
    deleted_user = cusor.fetchone()
    conn.commit()
    return deleted_user
