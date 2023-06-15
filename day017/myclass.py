class User:
    def __init__(self, Id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("123", "Gargoyle")

print(user_1.followers)