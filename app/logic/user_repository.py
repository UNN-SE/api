from app import log, serializer, auth
from app.models import User
from itsdangerous import BadSignature


class UserRepository:
    @staticmethod
    def authenticate(login, password):
        raise NotImplementedError

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        raise NotImplementedError


class UserRepositoryMock(UserRepository):
    @staticmethod
    def authenticate(login, password):
        return serializer.dumps(User.mock(1)).decode('utf-8')

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        try:
            log.info(serializer.loads(token))
            return User.mock(token)
        except BadSignature:
            if token:
                return User.mock(int(token))
        return False
