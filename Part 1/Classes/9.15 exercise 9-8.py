class User():
    def __init__(self, first_name, last_name, mbti, height):
        self.first = first_name
        self.last = last_name
        self.mbti = mbti
        self.height = height
        self.attempt = 0

    def describe_user(self):
        print(self.first.title() + ' ' + self.last.title() + "'s info:")
        print("- MBTI: " + self.mbti.upper())
        print("- Height: " + str(self.height) + " cm.")

    def greet_user(self):
        print("Hello, " + self.first.title() + ' ' + self.last.title() + ' !')

    def increment_login_attempts(self):
        self.attempt += 1
        print("Login attemps: " + str(self.attempt))

    def reset_login_attempts(self):
        self.attempt = 0
        print("Reset login attempts to 0")

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

sakol = Admin('sakolkiat', 'noirak', 'intj', 185 )
sakol.describe_user()

sakol.privileges.show_privileges()
print("\nAdding privileges...")
sakol_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

sakol.privileges.privileges =sakol_privileges
sakol.privileges.show_privileges()

