from fastapi import APIRouter
from services.auth_service import AuthService

router = APIRouter(
    responses={
        200: {'message': 'Authenticated'},
        201: {'message': 'Created'},
        400: {"message": "Bad Request"},
        404: {"message": "Resource not found"}
    }
)


@router.post('/login', summary="Sign in by getting user token")
def login():
    return AuthService.login()
