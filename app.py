from credentials import Credentials
from user import User

"""
This where we shall be running our app
"""

def createUserAccount(user_name,email,password):
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

def delete_user_credentials(account):
    account. delete_user_credentials()

def main():
    print("Hey there welcome to our Login app")
    print("Please enter your name")

    name = input()

    print(name +" Please use the following short codes: 'ca' to create account, 'si' to sign in, 'sa' to search accounts, 'ds' to display accounts  and 'x' to exit" )

    while True:

        input_code = input().lower()

        if input_code == "ca":
            print("Create a new account by keying in your account details")
            print("Key in your username")
            user_name = input()

            print('\n')
            print("Key in your email")
            email = input()

            print("Key in your password")

            password = input()

            save_new_user(createUserAccount(user_name,email,password))

            print("See your account details below")
            print(f"Username: {user_name},email: {email},password:{password}")

            print('\n')

            print(f"Welcome {user_name}, you have been succesfully logged in")
        elif input_code == 'si'
            print("Enter your account details")
            print("Account Name")
            account = input()

            print("Email")

            email  = input()

            print("Password")

            password = input()

            save_user_credentials(createCredentials(account,email,password))

        elif input_code == "ds":
            print(" Your account credentials are as follows}:")
            print ('\n')
            for creds in show_credentials():
                    print(f"{creds.account}\n {creds.email}\n {creds.password}")
            else: 
                print ('\n')
                print("Sorry, You do not have any accounts saved")

        elif short_code == "sa":
                print("Key in the name of the account you are looking for: ")
                userCred_input = input()
                if search_by_account(userCred_input):
                    account_search = search_by_account(userCred_inputserCred)
                    print(f"{account_search.account} {account_search.email} {account_search.password}")
                else: print("Sorry! The account does not exist!")
        elif input_code =="ex"
            print("Logging out..")
            break



    if __name__ == "__main__":
        main()






