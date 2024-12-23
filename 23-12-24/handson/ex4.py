class InvalidCountryException(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserRegistration:
    def __main__(self):
        username=input("Please input username ")
        usercountry=input("Please input user country ")
        try:
            self.register_user(username,usercountry)
        except InvalidCountryException as ic:
            print(ic.args[0])

    def register_user(self,username,usercountry):
        if usercountry.upper()!='INDIA':
            raise InvalidCountryException("User Outside India  cannot be registered")
        else:
            print("User registration done successfully")

ob=UserRegistration()
ob.__main__()