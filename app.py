from credentials import credentials
from user import User

"""
This where we shall be running our app
"""

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

def save_credentials(creds):
    """
    Display our credentials
    """
    creds.save_credentials()

def show_credentials():
    
    """displays all our saved credentials
    """
    return Credentials.displayCrendentials()

def search_by_account(account):

    return Credentials.searchByAccount(account)







