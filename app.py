from credentials import credentials
from user import User


def createUserAccount():
    """
    Create new account
    """
    new_user = User(user_name,email,password)
    return new_user

def save_new_user(user):
    """
    Saves new users
    """
    user.save_new_user()

def save_user_credentials(userCreds):

    userCreds.save_user_credentials()

def search_user_byname(user_name):
    return User.search_user(user_name)

def createCredentials(account,email,password):
    """
    creates credential objects
    """
    new_creds = Credentials(account,email,password)
    return new_creds

