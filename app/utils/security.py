from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= ["auto"])

def has_password(plain_password: str) -> str:
    pass

def verify_password(plain_password, hashed_password: str) -> bool:
    pass