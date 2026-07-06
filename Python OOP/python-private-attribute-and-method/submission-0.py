class PasswordManager:
    def __init__(self, password):
        self._password = password
        pass  
    
    # TODO: Implement the verify_password method
    def _get_password(self):
        return self._password

    def get_password(self):
        return self._get_password()

    def verify_password(self, user_password):
        saved_password = self.get_password()
        if saved_password == user_password:
            return(True)
        else:
            return(False)

# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
