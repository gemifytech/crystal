import sqlite3
from flask_restful import reqparse

class User():
    def __init__(self,_id,username, platform):
        self.id = _id
        self.username = username
        self.platform = platform
        #self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username =?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

    def post_user(self):
        if self.find_by_username(self.username):
            return False

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (self.username, self.platform))

        connection.commit()
        connection.close()

        return True

    def __repr__(self):
        return "ID: {}\nUsername: {}\nplatform: {}".format(self.id,self.username,self.platform)

class UserLogin():
    @classmethod
    def validate_user(cls, username, platform):
        user = User.find_by_username(username)
        if user and user.platform == platform:
            return user
        else:
            return None

#class TokenRefresh():
    #def refresh_token():
        #return