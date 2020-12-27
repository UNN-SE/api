from app import log, serializer, auth, db
from app.models import User, RevokedTokens
from itsdangerous import BadSignature
from sqlalchemy.exc import *


class UserRepository:
    @staticmethod
    def register(**kwargs):
        raise NotImplementedError

    @staticmethod
    def authenticate(login, password):
        raise NotImplementedError

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        raise NotImplementedError

    @staticmethod
    def logout(token):
        raise NotImplementedError


class UserRepositoryMock(UserRepository):
    @staticmethod
    def register(**kwargs):
        return 1

    @staticmethod
    def authenticate(login, password):
        return serializer.dumps(User.mock(1)).decode('utf-8')

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        try:
            log.info(serializer.loads(token))
            return User.mock(1)
        except BadSignature:
            if token:
                return User.mock(int(token))
        return False

    @staticmethod
    def logout(token):
        pass


class UserRepositoryDB(UserRepository):
    @staticmethod
    def register(**kwargs):
        new_user = User(email=kwargs['login'],
                        password=kwargs['password'],
                        phone=kwargs['phone'],
                        type=kwargs['type'])
        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user.id
        except SQLAlchemyError as exc:
            raise exc

    @staticmethod
    def authenticate(login, password):
        if User.query.filter_by(email=login, password=password).first():
            return serializer.dumps({'username': login}).decode('utf-8')
        return None

    @staticmethod
    @auth.verify_token
    def verify_token(token):
        try:
            if not RevokedTokens.query.filter_by(token=token).first():
                data = serializer.loads(token)
                return User.query.filter_by(email=data['username']).first()
        except BadSignature:
            pass
        return False

    @staticmethod
    def logout(token):
        try:
            db.session.add(RevokedTokens(token=token))
            db.session.commit()
            return True
        except SQLAlchemyError as exc:
            raise exc
