from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session
from models import User
from schemas import LoginRequest, TokenResponse
from security import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == data.username)).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Identifiants invalides")
    if user.is_blocked:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Compte bloqué")
    return TokenResponse(access_token=create_access_token(user.id))