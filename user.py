class User:
    """
    Class that generates instances of a user
    """

    user_list = []

    def __init__(self,user_name,password):
        """
        Init method to  help us define the properties of our objects
        """
        self.user_name = user_name
        self.password = password


    def save_user(self):
        """
        Save new user
        """

        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)


    @classmethod
    def search_by_username(cls,user_name):
        """
        Search by username
        """
        for user in user_list:
            if user.user_name == user_name:
                return user