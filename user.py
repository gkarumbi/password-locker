class User:
    """
    Class that generates instances of a user
    """

    def __init__(self,user_name,password):
        """
        Init method to  help us define the properties of our objects
        """
        self.user_name = user_name
        self.password = password