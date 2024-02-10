#!/bin/usr/python3
import sys
class User_sign():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
if __name__ == "__main__":
    print("Starting program...")
    username = input("Enter Username: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    print("Inputs collected...")
        
create_account = User_sign(username, email, password)
print("User account created...")
print("hello, welcome to kuku-poa")