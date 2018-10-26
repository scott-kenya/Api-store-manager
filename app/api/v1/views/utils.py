import re
import time

from abc import abstractmethod, ABCMeta
from passlib.handlers.pbkdf2 import pbkdf2_sha512


class Utils:
    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def password_checker(password):
        password_checker = re.match(r"^(?=.*[a-z])(?=.*[0-9]){6}", password)
        return True if password_checker else False

    @staticmethod
    def username_checker(username):
        username_checker = re.match(r"(?=^.{3,}$)(?=.*[a-z])^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$", username)
        return True if username_checker else False

    @staticmethod
    def timestamp():
        """Return the current timestamp as an integer."""
        return int(time.time())

    @staticmethod
    def hash_password(password):
    	return pbkdf2_sha512.hash(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)


