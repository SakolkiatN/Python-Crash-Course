from userss import User

class Admin(User):
    def __init__(self, first_name, last_name, mbti, height):
        super().__init__( first_name, last_name, mbti, height)
        #initialize an empty set of privileges
        self.privileges = Privileges()

class Privileges():
    """a class to store an admin's privileges."""
    def __init__(self, privileges = []):
        self.privileges = privileges
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
