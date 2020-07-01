from credentials import credentials
from user import User


def createUserAccount():
    """
    Create new account
    """
    new_user = User(user_name,email,password)
    return new_user

def save_user():
    """
    Saves users
    """