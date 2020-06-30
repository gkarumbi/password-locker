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
