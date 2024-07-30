class UserManager:
    def __init__(self):
        self.available_usernames = []
        self.assigned_usernames = {}

    def generate_usernames(self, prefix, start, end):
        self.available_usernames = [f"{prefix}{i:02d}" for i in range(start, end + 1)]
        self.assigned_usernames = {}

    def assign_username(self, workshop_username):
        # Convert input username to lowercase for case-insensitive check
        lowercase_workshop_username = workshop_username.lower()
        
        # Check if the lowercase version of the workshop username is already assigned
        for existing_workshop_username in self.assigned_usernames:
            if existing_workshop_username.lower() == lowercase_workshop_username:
                return self.assigned_usernames[existing_workshop_username]
        
        # If not already assigned, assign a new username
        if not self.available_usernames:
            return None
        
        username = self.available_usernames.pop(0)
        self.assigned_usernames[workshop_username] = username
        return username

user_manager = UserManager()
