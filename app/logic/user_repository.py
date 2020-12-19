from app import LOG, SERIALIZER, AUTH
from app.models import User
from itsdangerous import BadSignature


class UserRepository:
    @staticmethod
    def authenticate(login, password):
        raise NotImplementedError

    @staticmethod
    @AUTH.verify_token
    def verify_token(token):
        raise NotImplementedError


class UserRepositoryMock(UserRepository):
    @staticmethod
    def authenticate(login, password):
        return SERIALIZER.dumps(User.mock(1)).decode('utf-8')

    @staticmethod
    @AUTH.verify_token
    def verify_token(token):
        try:
            LOG.info(SERIALIZER.loads(token))
            return User.mock(1)
        except BadSignature:
            if token:
                return User.mock(int(token))
        return False
