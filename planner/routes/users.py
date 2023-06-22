from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter( tags=["User"],)
users = {}

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 유저입니다."
        )
    users[data.email] = data
    return {
        "message" : "유저 등록 성공!"
    }

@user_router.post("/signin")
async def sign_user_in(user:UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 메일주소입니다."
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="잘못된 비밀번호입니다.."
        )
    
    return{
        "message" : "로그인 성공"
    }