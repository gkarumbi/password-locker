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

    def deletePassword(self):
        """
        delete password method , deletes passwords into password list
        """
        Credentials.password_list.remove(self)

    @classmethod
    def searchByAccount(cls, account):
        """
        search for accounts
        """
        for Cred in cls.password_list:
            if Cred.account == account:
                return Cred

        # confirming details

   

if __name__ = "__main__":
    main()

    def createPassword(password):

        return password

    