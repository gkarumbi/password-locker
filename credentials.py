from user import user

class Credentials:
    """
    A Class that generates credentials
    """

    password_list = []

    def __init__(self,account,email,password):
        self.account = account
        self.email = email
        self.password = password

    def storePassword(self):
        """
        Store password method , stores passwords into password list
        """
        Credentials.password_list.append(self)

    


if __name__ = "__main__":
    main()

    def createPassword(password):

        return password

    